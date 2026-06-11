from __future__ import annotations

from dataclasses import dataclass
from math import hypot, pi, sin
from random import Random

from ui.class_visuals import (
    AttackVisualAction,
    VisualAction,
    frame_names_for_action,
)


@dataclass
class FloatingText:
    text: str
    x: float
    y: float
    color: str
    life: float = 0.9
    max_life: float = 0.9
    velocity_y: float = -24.0


@dataclass
class AmbientParticle:
    kind: str
    x: float
    y: float
    velocity_x: float
    velocity_y: float
    life: float
    max_life: float


@dataclass
class ArrowProjectile:
    start_x: float
    start_y: float
    end_x: float
    end_y: float
    speed: float = 720.0
    distance_travelled: float = 0.0
    active: bool = True

    @property
    def distance(self) -> float:
        return max(
            1.0,
            hypot(
                self.end_x - self.start_x,
                self.end_y - self.start_y,
            ),
        )

    @property
    def progress(self) -> float:
        return min(1.0, self.distance_travelled / self.distance)

    @property
    def x(self) -> float:
        return self.start_x + (self.end_x - self.start_x) * self.progress

    @property
    def y(self) -> float:
        return self.start_y + (self.end_y - self.start_y) * self.progress

    def update(self, dt: float) -> bool:
        if not self.active:
            return False
        self.distance_travelled += self.speed * max(0.0, dt)
        if self.progress < 1.0:
            return False
        self.active = False
        return True


class JourneySceneController:
    EXPLORE_SPEED = 60.0
    ENEMY_APPROACH_SPEED = 105.0
    SPEED_TRANSITION_SECONDS = 0.75
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
        hero_home_x: float = 102.0,
        enemy_home_x: float = 270.0,
        rng: Random | None = None,
        hero_attack_action: AttackVisualAction = "attack_melee",
    ) -> None:
        self.scene_width = scene_width
        self.hero_home_x = hero_home_x
        self.enemy_home_x = enemy_home_x
        self.rng = rng or Random()
        self.hero_attack_action = hero_attack_action

        self.phase = "explore"
        self.phase_time = 0.0
        self.background_scroll = 0.0
        self.world_speed_factor = 1.0
        self.encounter_distance = 0.0
        self.enemy_x = scene_width + 50.0
        self.hero_action: VisualAction = "walk"
        self.hero_frame_index = 0
        self.enemy_visible = False
        self.enemy_dead = False
        self.enemy_death_progress = 0.0
        self.reward_text = ""
        self.attack_kind: str | None = None
        self.attack_time = 0.0
        self.hit_target: str | None = None
        self.hit_time = 0.0
        self.floaters: list[FloatingText] = []
        self.projectiles: list[ArrowProjectile] = []
        self.pending_projectile_damage: int | None = None
        self.ranged_projectile_spawned = False
        self.pending_victory_text: str | None = None
        self.ambient_enabled = True
        self.ambient_time = 0.0
        self.next_ambient_event = self.rng.uniform(4.0, 7.0)
        self.ambient_particles: list[AmbientParticle] = []
        self.start_explore(resuming=False)

    @property
    def hero_frame(self) -> str:
        frames = frame_names_for_action(self.hero_action)
        return frames[self.hero_frame_index % len(frames)]

    @property
    def hero_x(self) -> float:
        if (
            self.attack_kind == "hero_attack"
            and self.hero_attack_action == "attack_melee"
        ):
            progress = min(1.0, self.attack_time / self.ATTACK_DURATION)
            return self.hero_home_x + sin(progress * pi) * self.HERO_DASH
        return self.hero_home_x

    @property
    def hero_y_offset(self) -> float:
        if self.phase == "explore":
            return -2.0 if self.hero_frame == "walk1" else 0.0
        if self.hero_action == "defeat":
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

    @property
    def world_speed_percent(self) -> int:
        return round(self.world_speed_factor * 100)

    def start_explore(self, resuming: bool = False) -> None:
        self.phase = "explore"
        self.phase_time = 0.0
        self.world_speed_factor = 0.0 if resuming else 1.0
        self.encounter_distance = self.rng.uniform(150.0, 230.0)
        self.enemy_x = self.scene_width + 50.0
        self.enemy_visible = False
        self.enemy_dead = False
        self.enemy_death_progress = 0.0
        self.reward_text = ""
        self.attack_kind = None
        self.hit_target = None
        self.hit_time = 0.0
        self.projectiles.clear()
        self.pending_projectile_damage = None
        self.ranged_projectile_spawned = False
        self.pending_victory_text = None
        self._set_hero_action("walk")

    def trigger_attack(self, kind: str, damage: int) -> None:
        if self.phase != "fight":
            return
        self.attack_kind = kind
        self.attack_time = 0.0
        if kind == "hero_attack":
            if self.hero_attack_action == "attack_ranged":
                self.pending_projectile_damage = damage
                self.ranged_projectile_spawned = False
                self.hit_target = None
                self.hit_time = 0.0
                return
            self._show_damage("enemy", damage)
        else:
            self._show_damage("hero", damage)

    def show_victory(self, reward_text: str) -> None:
        if (
            self.hero_attack_action == "attack_ranged"
            and (
                self.attack_kind == "hero_attack"
                or self.pending_projectile_damage is not None
                or any(projectile.active for projectile in self.projectiles)
            )
        ):
            self.pending_victory_text = reward_text
            return
        self._enter_victory(reward_text)

    def _enter_victory(
        self,
        reward_text: str,
        preserve_hit_feedback: bool = False,
    ) -> None:
        self.phase = "reward"
        self.phase_time = 0.0
        self.reward_text = reward_text
        self.enemy_dead = True
        self.enemy_death_progress = 0.0
        self.attack_kind = None
        if not preserve_hit_feedback:
            self.hit_target = None
            self.hit_time = 0.0
        self.pending_victory_text = None
        self._set_hero_action("victory")

    def show_defeat(self, text: str) -> None:
        self.phase = "reward"
        self.phase_time = 0.0
        self.reward_text = f"DERROTA\n{text}"
        self.enemy_visible = False
        self.attack_kind = None
        self.hit_target = None
        self.hit_time = 0.0
        self.projectiles.clear()
        self.pending_projectile_damage = None
        self.ranged_projectile_spawned = False
        self.pending_victory_text = None
        self._set_hero_action("defeat")

    def update(self, dt: float) -> list[str]:
        dt = max(0.0, min(0.05, dt))
        events: list[str] = []
        self.phase_time += dt
        events.extend(self._update_transients(dt))
        events.extend(self._update_projectiles(dt))
        self._update_ambient(dt)

        if self.phase == "explore":
            if self.world_speed_factor < 1.0:
                self.world_speed_factor = min(
                    1.0,
                    self.phase_time / self.SPEED_TRANSITION_SECONDS,
                )
            distance = self.EXPLORE_SPEED * self.world_speed_factor * dt
            self.background_scroll += distance
            self.encounter_distance -= distance
            frame_index = int(self.phase_time / self.WALK_FRAME_SECONDS) % 2
            self._set_hero_action("walk", frame_index)
            if self.encounter_distance <= 0:
                self.phase = "encounter"
                self.phase_time = 0.0
                self.enemy_x = self.scene_width + 45.0
                self.enemy_visible = True
                self._set_hero_action("idle")
                events.append("encounter")

        elif self.phase == "encounter":
            self.world_speed_factor = max(
                0.0,
                1.0 - self.phase_time / self.SPEED_TRANSITION_SECONDS,
            )
            self.background_scroll += (
                self.EXPLORE_SPEED * self.world_speed_factor * dt
            )
            self.enemy_x = max(
                self.enemy_home_x,
                self.enemy_x - self.ENEMY_APPROACH_SPEED * dt,
            )
            self._set_hero_action("idle")
            if (
                self.enemy_x <= self.enemy_home_x
                and self.world_speed_factor <= 0
            ):
                self.phase = "fight"
                self.phase_time = 0.0
                self.world_speed_factor = 0.0
                self._set_hero_action("combat_idle")
                events.append("fight")

        elif self.phase == "fight":
            if self.attack_kind is None:
                if self.hit_target == "hero" and self.hit_time > 0:
                    self._set_hero_action("hit")
                else:
                    self._set_hero_action("combat_idle")

        elif self.phase == "reward":
            if self.enemy_dead:
                self.enemy_death_progress = min(
                    1.0,
                    self.phase_time / self.DEATH_DURATION,
                )
                if self.enemy_death_progress >= 1.0:
                    self.enemy_visible = False
            if self.phase_time >= self.REWARD_DURATION:
                self.start_explore(resuming=True)
                events.append("explore")

        return events

    def _update_transients(self, dt: float) -> list[str]:
        events: list[str] = []
        if self.attack_kind is not None:
            self.attack_time += dt
            if self.attack_kind == "hero_attack":
                self._set_hero_action(
                    self.hero_attack_action,
                    0
                    if self.attack_time < self.ATTACK_HIT_TIME
                    else 1,
                )
                if (
                    self.hero_attack_action == "attack_ranged"
                    and self.attack_time >= self.ATTACK_HIT_TIME
                    and not self.ranged_projectile_spawned
                ):
                    self.projectiles.append(
                        ArrowProjectile(
                            start_x=self.hero_home_x + 30.0,
                            start_y=80.0,
                            end_x=self.enemy_x - 28.0,
                            end_y=82.0,
                        )
                    )
                    self.ranged_projectile_spawned = True
                    events.append("projectile_spawned")
            if self.attack_time >= self.ATTACK_DURATION:
                self.attack_kind = None
                self.attack_time = 0.0
                if self.phase == "fight":
                    self._set_hero_action("combat_idle")

        if self.hit_time > 0:
            self.hit_time = max(0.0, self.hit_time - dt)
            if self.hit_time == 0:
                self.hit_target = None

        for floater in self.floaters:
            floater.life -= dt
            floater.y += floater.velocity_y * dt
        self.floaters = [floater for floater in self.floaters if floater.life > 0]
        return events

    def _update_projectiles(self, dt: float) -> list[str]:
        events: list[str] = []
        for projectile in self.projectiles:
            if not projectile.update(dt):
                continue
            damage = self.pending_projectile_damage
            if damage is not None:
                self._show_damage("enemy", damage)
                self.pending_projectile_damage = None
            events.append("projectile_hit")
            if self.pending_victory_text is not None:
                self._enter_victory(
                    self.pending_victory_text,
                    preserve_hit_feedback=True,
                )
        self.projectiles = [
            projectile
            for projectile in self.projectiles
            if projectile.active
        ]
        return events

    def _show_damage(self, target: str, damage: int) -> None:
        self.hit_target = target
        self.hit_time = self.HIT_DURATION
        if target == "enemy":
            x = self.enemy_home_x
            color = "#ffd84a"
        else:
            x = self.hero_home_x
            color = "#e85a5a"
        self.floaters.append(FloatingText(f"-{damage}", x, 65.0, color))

    def _set_hero_action(
        self,
        action: VisualAction,
        frame_index: int = 0,
    ) -> None:
        self.hero_action = action
        self.hero_frame_index = frame_index

    def _update_ambient(self, dt: float) -> None:
        if (
            self.ambient_enabled
            and self.phase == "explore"
            and self.world_speed_factor > 0.45
        ):
            self.ambient_time += dt
            if self.ambient_time >= self.next_ambient_event:
                self.ambient_time = 0.0
                self.next_ambient_event = self.rng.uniform(4.0, 7.0)
                self._spawn_ambient_event()

        for particle in self.ambient_particles:
            particle.life -= dt
            particle.x += particle.velocity_x * dt
            particle.y += particle.velocity_y * dt
        self.ambient_particles = [
            particle
            for particle in self.ambient_particles
            if particle.life > 0
            and -30 < particle.x < self.scene_width + 40
            and -20 < particle.y < 180
        ]

    def _spawn_ambient_event(self) -> None:
        event = self.rng.choice(("crow", "leaves", "dust"))
        if event == "crow":
            count = self.rng.randint(2, 3)
            for index in range(count):
                life = 4.2
                self.ambient_particles.append(
                    AmbientParticle(
                        kind="crow",
                        x=self.scene_width + 18.0 + index * 20,
                        y=self.rng.uniform(32.0, 56.0) + index * 4,
                        velocity_x=self.rng.uniform(-78.0, -64.0),
                        velocity_y=self.rng.uniform(-2.0, 2.0),
                        life=life,
                        max_life=life,
                    )
                )
            return

        if event == "leaves":
            count = self.rng.randint(4, 7)
            for index in range(count):
                life = 3.4
                self.ambient_particles.append(
                    AmbientParticle(
                        kind="leaf",
                        x=self.scene_width + index * 12.0,
                        y=self.rng.uniform(65.0, 115.0),
                        velocity_x=self.rng.uniform(-58.0, -42.0),
                        velocity_y=self.rng.uniform(4.0, 10.0),
                        life=life,
                        max_life=life,
                    )
                )
            return

        count = self.rng.randint(4, 6)
        for index in range(count):
            life = 2.2
            self.ambient_particles.append(
                AmbientParticle(
                    kind="dust",
                    x=self.scene_width + index * 8.0,
                    y=self.rng.uniform(132.0, 148.0),
                    velocity_x=self.rng.uniform(-48.0, -32.0),
                    velocity_y=self.rng.uniform(-5.0, -1.0),
                    life=life,
                    max_life=life,
                )
            )
