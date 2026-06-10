from __future__ import annotations

from dataclasses import dataclass
from math import pi, sin
from random import Random


@dataclass
class FloatingText:
    text: str
    x: float
    y: float
    color: str
    life: float = 0.9
    max_life: float = 0.9
    velocity_y: float = -24.0


class JourneySceneController:
    EXPLORE_SPEED = 60.0
    ENCOUNTER_SCROLL_SPEED = 24.0
    ENEMY_APPROACH_SPEED = 105.0
    WALK_FRAME_SECONDS = 0.16
    ATTACK_DURATION = 0.42
    ATTACK_HIT_TIME = 0.16
    HERO_DASH = 22.0
    ENEMY_LUNGE = 16.0
    HIT_DURATION = 0.24
    DEATH_DURATION = 0.45
    REWARD_DURATION = 1.8

    def __init__(
        self,
        scene_width: float = 342.0,
        hero_home_x: float = 76.0,
        enemy_home_x: float = 270.0,
        rng: Random | None = None,
    ) -> None:
        self.scene_width = scene_width
        self.hero_home_x = hero_home_x
        self.enemy_home_x = enemy_home_x
        self.rng = rng or Random()

        self.phase = "explore"
        self.phase_time = 0.0
        self.background_scroll = 0.0
        self.encounter_distance = 0.0
        self.enemy_x = scene_width + 50.0
        self.hero_frame = "walk1"
        self.enemy_visible = False
        self.enemy_dead = False
        self.enemy_death_progress = 0.0
        self.reward_text = ""
        self.attack_kind: str | None = None
        self.attack_time = 0.0
        self.hit_target: str | None = None
        self.hit_time = 0.0
        self.floaters: list[FloatingText] = []
        self.start_explore()

    @property
    def hero_x(self) -> float:
        if self.attack_kind == "hero_attack":
            progress = min(1.0, self.attack_time / self.ATTACK_DURATION)
            return self.hero_home_x + sin(progress * pi) * self.HERO_DASH
        return self.hero_home_x

    @property
    def hero_y_offset(self) -> float:
        if self.phase == "explore":
            return -2.0 if self.hero_frame == "walk1" else 0.0
        if self.phase == "reward" and self.reward_text.startswith("DERROTA"):
            return 10.0
        return 0.0

    @property
    def enemy_draw_x(self) -> float:
        if self.attack_kind == "enemy_attack":
            progress = min(1.0, self.attack_time / self.ATTACK_DURATION)
            return self.enemy_x - sin(progress * pi) * self.ENEMY_LUNGE
        return self.enemy_x

    @property
    def enemy_y_offset(self) -> float:
        if self.enemy_dead:
            return self.enemy_death_progress * 24.0
        if self.phase == "encounter":
            return sin(self.phase_time * 12.0) * 1.5
        return 0.0

    @property
    def enemy_opacity(self) -> float:
        if not self.enemy_dead:
            return 1.0
        return max(0.0, 1.0 - self.enemy_death_progress)

    @property
    def hero_hit_flash(self) -> bool:
        return (
            self.hit_target == "hero"
            and self.hit_time > 0
            and int((self.HIT_DURATION - self.hit_time) / 0.055) % 2 == 0
        )

    @property
    def enemy_hit_flash(self) -> bool:
        return (
            self.hit_target == "enemy"
            and self.hit_time > 0
            and int((self.HIT_DURATION - self.hit_time) / 0.055) % 2 == 0
        )

    def start_explore(self) -> None:
        self.phase = "explore"
        self.phase_time = 0.0
        self.encounter_distance = self.rng.uniform(150.0, 230.0)
        self.enemy_x = self.scene_width + 50.0
        self.enemy_visible = False
        self.enemy_dead = False
        self.enemy_death_progress = 0.0
        self.reward_text = ""
        self.attack_kind = None
        self.hit_target = None
        self.hit_time = 0.0

    def trigger_attack(self, kind: str, damage: int) -> None:
        if self.phase != "fight":
            return
        self.attack_kind = kind
        self.attack_time = 0.0
        if kind == "hero_attack":
            self.hit_target = "enemy"
            x = self.enemy_home_x
            color = "#ffd84a"
        else:
            self.hit_target = "hero"
            x = self.hero_home_x
            color = "#e85a5a"
        self.hit_time = self.HIT_DURATION
        self.floaters.append(FloatingText(f"-{damage}", x, 65.0, color))

    def show_victory(self, reward_text: str) -> None:
        self.phase = "reward"
        self.phase_time = 0.0
        self.reward_text = reward_text
        self.enemy_dead = True
        self.enemy_death_progress = 0.0
        self.attack_kind = None
        self.hit_target = None
        self.hit_time = 0.0

    def show_defeat(self, text: str) -> None:
        self.phase = "reward"
        self.phase_time = 0.0
        self.reward_text = f"DERROTA\n{text}"
        self.enemy_visible = False
        self.attack_kind = None
        self.hit_target = None
        self.hit_time = 0.0

    def update(self, dt: float) -> list[str]:
        dt = max(0.0, min(0.05, dt))
        events: list[str] = []
        self.phase_time += dt
        self._update_transients(dt)

        if self.phase == "explore":
            self.background_scroll += self.EXPLORE_SPEED * dt
            self.encounter_distance -= self.EXPLORE_SPEED * dt
            frame_index = int(self.phase_time / self.WALK_FRAME_SECONDS) % 2
            self.hero_frame = "walk1" if frame_index == 0 else "walk2"
            if self.encounter_distance <= 0:
                self.phase = "encounter"
                self.phase_time = 0.0
                self.enemy_x = self.scene_width + 45.0
                self.enemy_visible = True
                self.hero_frame = "walk2"
                events.append("encounter")

        elif self.phase == "encounter":
            self.background_scroll += self.ENCOUNTER_SCROLL_SPEED * dt
            self.enemy_x = max(
                self.enemy_home_x,
                self.enemy_x - self.ENEMY_APPROACH_SPEED * dt,
            )
            frame_index = int(self.phase_time / 0.22) % 2
            self.hero_frame = "walk1" if frame_index == 0 else "walk2"
            if self.enemy_x <= self.enemy_home_x:
                self.phase = "fight"
                self.phase_time = 0.0
                self.hero_frame = "idle"
                events.append("fight")

        elif self.phase == "fight":
            if self.attack_kind is None:
                if self.hit_target == "hero" and self.hit_time > 0:
                    self.hero_frame = "hit"
                else:
                    self.hero_frame = "idle"

        elif self.phase == "reward":
            if self.enemy_dead:
                self.enemy_death_progress = min(
                    1.0,
                    self.phase_time / self.DEATH_DURATION,
                )
                if self.enemy_death_progress >= 1.0:
                    self.enemy_visible = False
            if self.phase_time >= self.REWARD_DURATION:
                self.start_explore()
                events.append("explore")

        return events

    def _update_transients(self, dt: float) -> None:
        if self.attack_kind is not None:
            self.attack_time += dt
            if self.attack_kind == "hero_attack":
                self.hero_frame = (
                    "attack1"
                    if self.attack_time < self.ATTACK_HIT_TIME
                    else "attack2"
                )
            if self.attack_time >= self.ATTACK_DURATION:
                self.attack_kind = None
                self.attack_time = 0.0
                if self.phase == "fight":
                    self.hero_frame = "idle"

        if self.hit_time > 0:
            self.hit_time = max(0.0, self.hit_time - dt)
            if self.hit_time == 0:
                self.hit_target = None

        for floater in self.floaters:
            floater.life -= dt
            floater.y += floater.velocity_y * dt
        self.floaters = [floater for floater in self.floaters if floater.life > 0]
