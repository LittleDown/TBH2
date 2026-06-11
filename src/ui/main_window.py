from __future__ import annotations

from collections import deque
from pathlib import Path
from random import Random
from time import perf_counter
import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from application.game_session import GameSession
from application.save_coordinator import SaveCoordinator
from game_state import GameState
from save.save_manager import SaveManager
from ui.class_visuals import (
    RENDER_FRAME_NAMES,
    resolve_visual_asset,
    visual_profile_for,
)
from ui.expanded_window import ExpandedWindow
from ui.journey_scene import JourneySceneController


class MainWindow(ctk.CTk):
    COMBAT_INTERVAL_MS = 800
    ANIMATION_FRAME_MS = 33
    SAVE_INTERVAL_MS = 10_000
    COLORS = {
        "window": "#0d0b12",
        "panel": "#17131f",
        "panel_alt": "#211a2b",
        "panel_light": "#2b2236",
        "gold": "#e0a640",
        "gold_dark": "#81551a",
        "text": "#f2edf5",
        "muted": "#9c91a5",
        "hp": "#c64355",
        "xp": "#3977c3",
        "success": "#285746",
    }
    ENEMY_SPRITES = {
        "Goblin": "goblin",
        "Lobo": "wolf",
        "Esqueleto": "skeleton",
    }
    MAP_THEMES = (
        ("#879e9b", "#516541", "#9a7953", "road"),
        ("#587565", "#2e4b35", "#745d43", "forest"),
        ("#9b7657", "#5d4d35", "#8a6a48", "camp"),
        ("#718294", "#4d5a42", "#817258", "hills"),
        ("#515463", "#313541", "#665f5c", "cemetery"),
        ("#77766e", "#4d5041", "#756b55", "ruins"),
        ("#6f8791", "#3f5b51", "#80694d", "bridge"),
        ("#514d58", "#36333c", "#62564e", "fortress"),
        ("#7e6c65", "#4d433e", "#76624d", "gate"),
        ("#3f3948", "#29262f", "#594b45", "fortress"),
    )

    def __init__(self, state: GameState, save_manager: SaveManager) -> None:
        super().__init__()
        self.game_state = state
        self.hero = state.hero
        self.save_manager = save_manager
        self.combat = GameSession(state)
        self.save_coordinator = SaveCoordinator(state, save_manager)
        self.log_lines: deque[str] = deque(maxlen=1)
        self.nav_buttons: dict[str, ctk.CTkButton] = {}
        self.expanded_window: ExpandedWindow | None = None
        visual_profile = visual_profile_for(self.hero.class_id)
        self.journey = JourneySceneController(
            hero_attack_action=visual_profile.attack_action
        )
        self.last_frame_time = perf_counter()
        self.scene_map_index = -1
        self.road_parallax = self._create_road_parallax()
        self.display_enemy_name = ""
        self.display_enemy_level = 1
        self.display_enemy_is_boss = False
        self.display_enemy_category = "common"
        self.display_enemy_key = "goblin"
        self.display_enemy_hp = 1
        self.display_enemy_max_hp = 1
        self.pending_display_enemy_hp: int | None = None
        self._capture_display_enemy()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("TBH2 - TaskBar Hero 2")
        self.resizable(False, False)
        self.configure(fg_color=self.COLORS["window"])
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._position_as_companion()
        self.sprites = self._load_sprites()

        self._build_ui()
        self._append_log(
            f"{self.hero.name} iniciou sua jornada por "
            f"{self.game_state.campaign.current_map}."
        )
        self._refresh()
        self.after(self.ANIMATION_FRAME_MS, self._animation_loop)
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _position_as_companion(self) -> None:
        width, height = 360, 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = max(0, screen_width - width - 18)
        y = max(0, screen_height - height - 70)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def _load_sprites(self) -> dict[str, ctk.CTkImage]:
        asset_root = Path(__file__).resolve().parents[1] / "assets"
        asset_dir = asset_root / "sprites"
        sprites: dict[str, ctk.CTkImage] = {}
        self.scene_sprites: dict[str, ImageTk.PhotoImage] = {}
        self.scene_hero_frames: dict[str, ImageTk.PhotoImage] = {}
        sizes = {
            "hero": (82, 82),
            "goblin": (82, 82),
            "wolf": (82, 82),
            "skeleton": (82, 82),
            "boss": (82, 82),
            "loot_chest": (22, 22),
        }
        for name, size in sizes.items():
            path = asset_dir / f"{name}.png"
            if not path.exists():
                continue
            with Image.open(path) as source:
                image = source.convert("RGBA").copy()
            sprites[name] = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=size,
            )
            scene_size = (78, 78) if name != "boss" else (84, 84)
            scene_image = image.resize(scene_size, Image.Resampling.NEAREST)
            self.scene_sprites[name] = ImageTk.PhotoImage(scene_image)

        profile_path = resolve_visual_asset(
            asset_root,
            self.hero.class_id,
            "front",
        )
        if profile_path is not None:
            with Image.open(profile_path) as source:
                profile_image = source.convert("RGBA").copy()
            sprites["hero"] = ctk.CTkImage(
                light_image=profile_image,
                dark_image=profile_image,
                size=(82, 82),
            )

        for frame_name in RENDER_FRAME_NAMES:
            path = resolve_visual_asset(
                asset_root,
                self.hero.class_id,
                frame_name,
            )
            if path is None:
                continue
            with Image.open(path) as source:
                frame = source.convert("RGBA").copy()
            frame.thumbnail((84, 84), Image.Resampling.LANCZOS)
            canvas = Image.new("RGBA", (88, 88), (0, 0, 0, 0))
            canvas.alpha_composite(
                frame,
                ((88 - frame.width) // 2, 88 - frame.height),
            )
            self.scene_hero_frames[frame_name] = ImageTk.PhotoImage(canvas)

        world_dir = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "world"
            / "abandoned_road"
        )
        self.world_sprites: dict[str, ImageTk.PhotoImage] = {}
        world_sizes = {
            "tree_01": (46, 60),
            "tree_02": (50, 64),
            "tree_03": (42, 64),
            "rock_01": (31, 25),
            "rock_02": (28, 22),
            "sign_01": (31, 40),
            "grass_01": (23, 24),
            "campfire_01": (34, 19),
            "sword_01": (25, 42),
            "cart_01": (49, 36),
            "banner_01": (29, 41),
            "tracks_01": (44, 29),
        }
        for name, maximum_size in world_sizes.items():
            path = world_dir / f"{name}.png"
            if not path.exists():
                continue
            with Image.open(path) as source:
                image = source.convert("RGBA").copy()
            image.thumbnail(maximum_size, Image.Resampling.LANCZOS)
            self.world_sprites[name] = ImageTk.PhotoImage(image)
        return sprites

    def _build_ui(self) -> None:
        self._build_header()
        self._build_combat_area()
        self._build_last_action()
        self._build_compact_summary()
        self._build_navigation()

    @staticmethod
    def _create_road_parallax() -> dict[str, list[dict[str, float | str]]]:
        rng = Random(20260610)
        far: list[dict[str, float | str]] = []
        for x in range(0, 760, 105):
            far.append(
                {
                    "kind": rng.choice(("mountain_01", "mountain_02")),
                    "x": float(x + rng.randint(-18, 18)),
                    "y": float(rng.randint(65, 74)),
                    "scale": rng.uniform(0.8, 1.2),
                }
            )
        far.append({"kind": "castle_01", "x": 515.0, "y": 66.0, "scale": 1.0})

        middle: list[dict[str, float | str]] = []
        x = 10
        while x < 640:
            middle.append(
                {
                    "kind": rng.choice(
                        ("tree_01", "tree_02", "tree_03", "fence_01")
                    ),
                    "x": float(x),
                    "y": float(rng.randint(91, 104)),
                    "scale": rng.uniform(0.8, 1.15),
                }
            )
            x += rng.randint(55, 88)

        foreground: list[dict[str, float | str]] = []
        x = 5
        while x < 520:
            foreground.append(
                {
                    "kind": rng.choice(
                        (
                            "rock_01",
                            "rock_02",
                            "grass_01",
                            "grass_01",
                            "sign_01",
                        )
                    ),
                    "x": float(x),
                    "y": float(rng.randint(111, 151)),
                    "scale": rng.uniform(0.75, 1.2),
                }
            )
            x += rng.randint(32, 54)

        story = [
            {"kind": "tracks_01", "x": 290.0, "y": 149.0, "scale": 1.0},
            {"kind": "sword_01", "x": 650.0, "y": 145.0, "scale": 1.0},
            {"kind": "campfire_01", "x": 1010.0, "y": 143.0, "scale": 1.0},
            {"kind": "cart_01", "x": 1390.0, "y": 142.0, "scale": 1.0},
            {"kind": "banner_01", "x": 1810.0, "y": 142.0, "scale": 1.0},
        ]

        return {
            "far": far,
            "middle": middle,
            "foreground": foreground,
            "story": story,
        }

    def _build_header(self) -> None:
        header = ctk.CTkFrame(
            self,
            height=52,
            fg_color="#1e1728",
            border_width=1,
            border_color="#33263f",
            corner_radius=0,
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        brand = ctk.CTkFrame(header, fg_color="transparent")
        brand.pack(side="left", padx=11, pady=5)
        ctk.CTkLabel(
            brand,
            text="◆ TBH2",
            font=ctk.CTkFont(family="Consolas", size=21, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(anchor="w")
        ctk.CTkLabel(
            brand,
            text="TASKBAR IDLE RPG",
            font=ctk.CTkFont(family="Consolas", size=8, weight="bold"),
            text_color=self.COLORS["muted"],
        ).pack(anchor="w")

        self.header_stats = ctk.CTkLabel(
            header,
            text="",
            justify="right",
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
        )
        self.header_stats.pack(side="right", padx=11)

        self.map_header = ctk.CTkLabel(
            self,
            text="",
            height=27,
            fg_color="#121019",
            text_color="#d8c9df",
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
        )
        self.map_header.pack(fill="x")

    def _build_combat_area(self) -> None:
        self.journey_frame = ctk.CTkFrame(
            self,
            height=177,
            fg_color=self.COLORS["panel"],
            border_width=1,
            border_color="#302638",
            corner_radius=8,
        )
        self.journey_frame.pack(fill="x", padx=8, pady=(6, 0))
        self.journey_frame.pack_propagate(False)

        self.scene = tk.Canvas(
            self.journey_frame,
            width=342,
            height=173,
            highlightthickness=0,
            bd=0,
            background="#17131f",
        )
        self.scene.pack(fill="both", expand=True, padx=1, pady=1)
        self._draw_environment(force=True)

        hero_image = self.scene_hero_frames.get(
            "walk1",
            self.scene_sprites.get("hero"),
        )
        self.scene_hero = self.scene.create_image(
            self.journey.hero_home_x,
            90,
            image=hero_image,
            anchor="center",
            tags=("actor",),
        )
        self.scene_enemy = self.scene.create_image(
            270,
            90,
            image=self.scene_sprites.get("goblin"),
            anchor="center",
            state="hidden",
            tags=("actor",),
        )
        self.scene_status = self.scene.create_text(
            171,
            12,
            text="EXPLORANDO",
            fill=self.COLORS["gold"],
            font=("Consolas", 9, "bold"),
            tags=("hud",),
        )
        self.scene_reward = self.scene.create_text(
            171,
            37,
            text="",
            fill="#f3d79b",
            font=("Consolas", 9, "bold"),
            width=300,
            justify="center",
            state="hidden",
            tags=("hud",),
        )
        self.scene_hero_name = self.scene.create_text(
            72,
            130,
            text="",
            fill="#f2edf5",
            font=("Consolas", 9, "bold"),
            tags=("hud",),
        )
        self.scene_enemy_name = self.scene.create_text(
            270,
            130,
            text="",
            fill="#f2edf5",
            font=("Consolas", 9, "bold"),
            state="hidden",
            tags=("hud",),
        )
        self.scene_hero_hp_bg = self.scene.create_rectangle(
            18, 140, 126, 147, fill="#3b303e", outline="", tags=("hud",)
        )
        self.scene_hero_hp = self.scene.create_rectangle(
            18, 140, 126, 147, fill=self.COLORS["hp"], outline="", tags=("hud",)
        )
        self.scene_enemy_hp_bg = self.scene.create_rectangle(
            216,
            140,
            324,
            147,
            fill="#3b303e",
            outline="",
            state="hidden",
            tags=("hud",),
        )
        self.scene_enemy_hp = self.scene.create_rectangle(
            216,
            140,
            324,
            147,
            fill=self.COLORS["hp"],
            outline="",
            state="hidden",
            tags=("hud",),
        )
        self.scene.tag_raise("actor")
        self.scene.tag_raise("hud")

    def _draw_environment(self, force: bool = False) -> None:
        map_index = self.game_state.campaign.map_index
        if not force and map_index == self.scene_map_index:
            return
        self.scene_map_index = map_index
        sky, ground, path, feature = self.MAP_THEMES[map_index]
        canvas = self.scene
        canvas.delete("environment")
        canvas.create_rectangle(
            0, 0, 342, 173, fill=sky, outline="", tags=("environment",)
        )
        canvas.create_rectangle(
            0, 70, 342, 173, fill=ground, outline="", tags=("environment",)
        )
        canvas.create_polygon(
            0,
            120,
            342,
            105,
            342,
            154,
            0,
            162,
            fill=path,
            outline="",
            tags=("environment",),
        )

        if feature == "road":
            self._draw_fields()
        elif feature == "forest":
            self._draw_forest()
        elif feature == "camp":
            self._draw_camp()
        elif feature == "hills":
            self._draw_hills()
        elif feature == "cemetery":
            self._draw_cemetery()
        elif feature == "bridge":
            self._draw_bridge()
        elif feature == "ruins":
            self._draw_ruins()
        elif feature == "fog":
            self._draw_fog()
        elif feature == "gate":
            self._draw_gate()
        else:
            self._draw_fortress()
        canvas.tag_lower("environment")

    def _draw_motion_layer(self) -> None:
        self.scene.delete("motion")
        if self.game_state.campaign.map_index == 0:
            self._draw_road_parallax()
            return

        offset = int(self.journey.background_scroll) % 48
        _, ground, path, feature = self.MAP_THEMES[
            self.game_state.campaign.map_index
        ]
        accent = {
            "road": "#d4b96c",
            "forest": "#78945f",
            "camp": "#bf8052",
            "hills": "#9a9a72",
            "cemetery": "#8d8e98",
            "bridge": "#b39767",
            "ruins": "#9b9688",
            "fog": "#d4d8d6",
            "gate": "#a18d7f",
            "fortress": "#8a828e",
        }[feature]
        for index in range(9):
            x = index * 48 - offset - 20
            self.scene.create_line(
                x,
                151,
                x + 15,
                149,
                fill=accent,
                width=2,
                tags=("motion",),
            )
            self.scene.create_oval(
                x + 24,
                111,
                x + 29,
                115,
                fill=ground,
                outline=path,
                tags=("motion",),
            )
        self.scene.tag_raise("motion", "environment")
        self.scene.tag_lower("motion", "actor")

    def _draw_road_parallax(self) -> None:
        layers = (
            ("far", 0.20, 760.0, "parallax_far"),
            ("middle", 0.50, 640.0, "parallax_middle"),
            ("foreground", 1.00, 520.0, "parallax_foreground"),
            ("story", 1.00, 2200.0, "parallax_story"),
        )
        for layer_name, speed, cycle, tag in layers:
            for element in self.road_parallax[layer_name]:
                base_x = float(element["x"])
                x = (
                    base_x - self.journey.background_scroll * speed + 90
                ) % cycle - 90
                self._draw_road_element(
                    kind=str(element["kind"]),
                    x=x,
                    y=float(element["y"]),
                    scale=float(element["scale"]),
                    tag=tag,
                )

        self.scene.tag_raise("parallax_far", "environment")
        self.scene.tag_raise("parallax_middle", "parallax_far")
        self.scene.tag_raise("parallax_foreground", "parallax_middle")
        self.scene.tag_raise("parallax_story", "parallax_foreground")
        self.scene.tag_lower("parallax_story", "actor")

    def _draw_road_element(
        self,
        kind: str,
        x: float,
        y: float,
        scale: float,
        tag: str,
    ) -> None:
        tags = ("motion", tag)
        sprite = self.world_sprites.get(kind)
        if sprite is not None:
            self.scene.create_image(
                x,
                y,
                image=sprite,
                anchor="s",
                tags=tags,
            )
            return

        if kind.startswith("mountain"):
            width = (88 if kind == "mountain_01" else 112) * scale
            height = (27 if kind == "mountain_01" else 34) * scale
            color = "#647977" if kind == "mountain_01" else "#596f6d"
            self.scene.create_polygon(
                x - width / 2,
                y,
                x - width * 0.12,
                y - height,
                x + width * 0.12,
                y - height * 0.45,
                x + width / 2,
                y,
                fill=color,
                outline="",
                tags=tags,
            )
            return

        if kind == "castle_01":
            self.scene.create_rectangle(
                x - 18 * scale,
                y - 18 * scale,
                x + 18 * scale,
                y,
                fill="#566866",
                outline="",
                tags=tags,
            )
            for tower_x in (x - 19 * scale, x + 10 * scale):
                self.scene.create_rectangle(
                    tower_x,
                    y - 27 * scale,
                    tower_x + 9 * scale,
                    y,
                    fill="#50615f",
                    outline="",
                    tags=tags,
                )
            return

        if kind.startswith("tree"):
            height = {
                "tree_01": 38,
                "tree_02": 47,
                "tree_03": 32,
            }[kind] * scale
            crown = {
                "tree_01": "#365b38",
                "tree_02": "#294b31",
                "tree_03": "#486a3d",
            }[kind]
            self.scene.create_rectangle(
                x - 3 * scale,
                y - height * 0.55,
                x + 3 * scale,
                y,
                fill="#5a402d",
                outline="",
                tags=tags,
            )
            self.scene.create_oval(
                x - 16 * scale,
                y - height,
                x + 16 * scale,
                y - height * 0.35,
                fill=crown,
                outline="",
                tags=tags,
            )
            return

        if kind == "fence_01":
            self.scene.create_line(
                x - 21 * scale,
                y - 13 * scale,
                x + 21 * scale,
                y - 10 * scale,
                fill="#71573b",
                width=2,
                tags=tags,
            )
            for post_x in (x - 18 * scale, x, x + 18 * scale):
                self.scene.create_line(
                    post_x,
                    y - 20 * scale,
                    post_x,
                    y,
                    fill="#6b5138",
                    width=2,
                    tags=tags,
                )
            return

        if kind.startswith("rock"):
            width = (13 if kind == "rock_01" else 20) * scale
            height = (7 if kind == "rock_01" else 10) * scale
            self.scene.create_oval(
                x - width / 2,
                y - height,
                x + width / 2,
                y,
                fill="#696961",
                outline="#4e514d",
                tags=tags,
            )
            return

        if kind == "sign_01":
            self.scene.create_line(
                x,
                y - 22 * scale,
                x,
                y,
                fill="#684a31",
                width=3,
                tags=tags,
            )
            self.scene.create_polygon(
                x - 2 * scale,
                y - 23 * scale,
                x + 17 * scale,
                y - 21 * scale,
                x + 11 * scale,
                y - 14 * scale,
                x - 2 * scale,
                y - 16 * scale,
                fill="#89623c",
                outline="",
                tags=tags,
            )
            return

        self.scene.create_line(
            x - 6 * scale,
            y,
            x - 2 * scale,
            y - 10 * scale,
            x,
            y,
            x + 5 * scale,
            y - 12 * scale,
            fill="#78914c",
            width=2,
            tags=tags,
        )

    def _draw_ambient_events(self) -> None:
        self.scene.delete("ambient")
        for particle in self.journey.ambient_particles:
            x, y = particle.x, particle.y
            if particle.kind == "crow":
                wing_up = int((particle.max_life - particle.life) * 9) % 2 == 0
                wing_y = y - 3 if wing_up else y + 2
                self.scene.create_line(
                    x - 5,
                    wing_y,
                    x,
                    y,
                    x + 5,
                    wing_y,
                    fill="#1d2020",
                    width=2,
                    smooth=True,
                    tags=("ambient",),
                )
            elif particle.kind == "leaf":
                self.scene.create_oval(
                    x - 2,
                    y - 1,
                    x + 2,
                    y + 1,
                    fill="#8b7438",
                    outline="#5d5d2f",
                    tags=("ambient",),
                )
            else:
                self.scene.create_oval(
                    x - 4,
                    y - 2,
                    x + 4,
                    y + 2,
                    fill="#c6aa79",
                    outline="",
                    stipple="gray50",
                    tags=("ambient",),
                )
        if self.scene.find_withtag("ambient"):
            if self.scene.find_withtag("parallax_middle"):
                self.scene.tag_raise("ambient", "parallax_middle")
            elif self.scene.find_withtag("environment"):
                self.scene.tag_raise("ambient", "environment")

            if self.scene.find_withtag("actor"):
                self.scene.tag_lower("ambient", "actor")

    def _draw_fields(self) -> None:
        self.scene.create_oval(
            235, 24, 282, 48, fill="#d7dfcf", outline="", tags=("environment",)
        )

    def _draw_forest(self) -> None:
        for x in (18, 52, 292, 326):
            self.scene.create_rectangle(
                x - 4, 48, x + 4, 103, fill="#4c3829", outline="", tags=("environment",)
            )
            self.scene.create_oval(
                x - 22, 20, x + 22, 72, fill="#274c32", outline="", tags=("environment",)
            )

    def _draw_camp(self) -> None:
        self.scene.create_polygon(
            20, 105, 52, 64, 84, 105, fill="#7c4931", outline="", tags=("environment",)
        )
        self.scene.create_line(
            226, 96, 248, 66, 270, 96, fill="#e5a044", width=3, tags=("environment",)
        )
        self.scene.create_oval(
            239, 80, 257, 101, fill="#d76c2f", outline="", tags=("environment",)
        )

    def _draw_hills(self) -> None:
        self.scene.create_oval(
            -60, 34, 155, 132, fill="#5e6b55", outline="", tags=("environment",)
        )
        self.scene.create_oval(
            205, 28, 390, 128, fill="#596650", outline="", tags=("environment",)
        )

    def _draw_cemetery(self) -> None:
        for x, y in ((24, 92), (58, 82), (287, 86), (319, 96)):
            self.scene.create_rectangle(
                x, y - 24, x + 15, y, fill="#777987", outline="", tags=("environment",)
            )
            self.scene.create_oval(
                x, y - 31, x + 15, y - 17, fill="#777987", outline="", tags=("environment",)
            )

    def _draw_bridge(self) -> None:
        self.scene.create_rectangle(
            0, 115, 342, 173, fill="#34545c", outline="", tags=("environment",)
        )
        for x in range(0, 342, 28):
            self.scene.create_rectangle(
                x, 112, x + 24, 150, fill="#80694d", outline="#4a3829", tags=("environment",)
            )

    def _draw_ruins(self) -> None:
        for x, height in ((18, 50), (46, 34), (286, 46), (316, 62)):
            self.scene.create_rectangle(
                x, 104 - height, x + 19, 104, fill="#77746b", outline="", tags=("environment",)
            )

    def _draw_fog(self) -> None:
        for y in (40, 65, 92):
            self.scene.create_line(
                5, y, 337, y - 5, fill="#b1b6b6", width=4, tags=("environment",)
            )

    def _draw_gate(self) -> None:
        self.scene.create_rectangle(
            266, 38, 337, 112, fill="#63564e", outline="", tags=("environment",)
        )
        self.scene.create_arc(
            278, 55, 325, 122, start=0, extent=180, fill="#25232a", outline="", tags=("environment",)
        )

    def _draw_fortress(self) -> None:
        self.scene.create_rectangle(
            230, 28, 341, 113, fill="#4a4650", outline="", tags=("environment",)
        )
        for x in (230, 260, 290, 320):
            self.scene.create_rectangle(
                x, 18, x + 16, 44, fill="#4a4650", outline="", tags=("environment",)
            )
        self.scene.create_arc(
            270, 62, 315, 126, start=0, extent=180, fill="#201e25", outline="", tags=("environment",)
        )

    def _build_last_action(self) -> None:
        action = ctk.CTkFrame(
            self,
            height=43,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#332840",
            corner_radius=6,
        )
        action.pack(fill="x", padx=8, pady=6)
        action.pack_propagate(False)
        ctk.CTkLabel(
            action,
            text="ÚLTIMA AÇÃO",
            width=78,
            font=ctk.CTkFont(family="Consolas", size=8, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(side="left", padx=(7, 2))
        self.event_log = ctk.CTkLabel(
            action,
            text="",
            justify="left",
            anchor="w",
            wraplength=245,
            font=ctk.CTkFont(size=9),
        )
        self.event_log.pack(side="left", fill="both", expand=True, padx=(0, 7))

    def _build_compact_summary(self) -> None:
        summary = ctk.CTkFrame(
            self,
            fg_color=self.COLORS["panel"],
            border_width=1,
            border_color="#2c2434",
            corner_radius=7,
        )
        summary.pack(fill="both", expand=True, padx=8)

        self.hero_profile_sprite = ctk.CTkLabel(
            summary,
            text="",
            width=92,
            height=112,
        )
        self.hero_profile_sprite.pack(side="left", padx=(8, 4), pady=7)

        information = ctk.CTkFrame(summary, fg_color="transparent")
        information.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(2, 8),
            pady=8,
        )
        self.hero_stats = ctk.CTkLabel(
            information,
            text="",
            justify="left",
            anchor="nw",
            font=ctk.CTkFont(family="Consolas", size=10),
        )
        self.hero_stats.pack(fill="both", expand=True)
        self.build_summary = ctk.CTkLabel(
            information,
            text="",
            height=27,
            fg_color=self.COLORS["panel_light"],
            corner_radius=5,
            font=ctk.CTkFont(
                family="Consolas",
                size=9,
                weight="bold",
            ),
            text_color="#d7cedc",
        )
        self.build_summary.pack(fill="x", pady=(5, 0))

    def _build_navigation(self) -> None:
        navigation = ctk.CTkFrame(
            self,
            height=48,
            fg_color="#1e1728",
            border_width=1,
            border_color="#33263f",
            corner_radius=0,
        )
        navigation.pack(side="bottom", fill="x", pady=(6, 0))
        navigation.pack_propagate(False)

        panel_names = (
            ("Herói", "Herói"),
            ("Mochila", "Mochila"),
            ("Mapa", "Mapa"),
        )
        for button_text, panel_name in panel_names:
            button = ctk.CTkButton(
                navigation,
                text=button_text,
                width=104,
                height=32,
                fg_color="#30253e",
                hover_color="#49365b",
                font=ctk.CTkFont(size=10, weight="bold"),
                command=lambda name=panel_name: self._open_expanded_panel(name),
            )
            button.pack(side="left", expand=True, padx=3, pady=8)
            self.nav_buttons[panel_name] = button

    def _open_expanded_panel(self, panel_name: str) -> None:
        if (
            self.expanded_window is None
            or not self.expanded_window.winfo_exists()
        ):
            self.expanded_window = ExpandedWindow(
                self,
                self.game_state,
                self._equip_item,
            )
        self.expanded_window.show(panel_name)
        for name, button in self.nav_buttons.items():
            button.configure(
                fg_color=self.COLORS["gold_dark"]
                if name == panel_name
                else "#30253e"
            )

    def _animation_loop(self) -> None:
        now = perf_counter()
        delta_time = now - self.last_frame_time
        self.last_frame_time = now
        self.journey.ambient_enabled = (
            self.game_state.campaign.map_index == 0
        )

        for event in self.journey.update(delta_time):
            if event == "encounter":
                self._capture_display_enemy()
                encounter_text = (
                    f"Chefe {self.display_enemy_name} bloqueou a passagem!"
                    if self.display_enemy_is_boss
                    else f"{self.hero.name} encontrou "
                    f"{self.display_enemy_name}."
                )
                self._append_log(encounter_text)
            elif event == "fight":
                self._append_log(
                    f"Combate iniciado contra {self.display_enemy_name}."
                )
                self.after(200, self._combat_tick)
            elif event == "projectile_hit":
                if self.pending_display_enemy_hp is not None:
                    self.display_enemy_hp = self.pending_display_enemy_hp
                    self.pending_display_enemy_hp = None
            elif event == "explore":
                self._append_log(f"{self.hero.name} retomou a caminhada.")
            self._refresh()

        self._refresh_scene()
        self.after(self.ANIMATION_FRAME_MS, self._animation_loop)

    def _combat_tick(self) -> None:
        if self.journey.phase != "fight":
            return
        enemy_before_tick = self.combat.enemy
        enemy_hp_before_tick = enemy_before_tick.current_hp
        events = self.combat.tick()
        self._capture_display_enemy(enemy_before_tick)

        victory_event = next(
            (event for event in events if event.kind == "victory"),
            None,
        )
        defeat_event = next(
            (event for event in events if event.kind == "defeat"),
            None,
        )
        attack_event = next(
            (
                event
                for event in events
                if event.kind in {"hero_attack", "enemy_attack"}
            ),
            None,
        )
        if attack_event is not None:
            self._append_log(attack_event.message)
            self.journey.trigger_attack(
                attack_event.kind,
                attack_event.amount or 0,
            )
            if (
                attack_event.kind == "hero_attack"
                and self.journey.hero_attack_action == "attack_ranged"
            ):
                self.pending_display_enemy_hp = self.display_enemy_hp
                self.display_enemy_hp = enemy_hp_before_tick
        self.save_coordinator.handle_events(events)

        if victory_event is not None:
            loot_event = next(
                (
                    event
                    for event in events
                    if event.kind == "loot" and event.item is not None
                ),
                None,
            )
            reward_text = victory_event.message
            if loot_event is not None:
                reward_text += f"\nLoot: {loot_event.item.name}"
            self._append_log(reward_text.replace("\n", "  •  "))
            self.journey.show_victory(reward_text)
            self._refresh()
            return

        if defeat_event is not None:
            reward_text = "O aventureiro caiu, mas retornará à estrada."
            self._append_log(defeat_event.message)
            self.journey.show_defeat(reward_text)
            self._refresh()
            return

        self._refresh()
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)

    def _capture_display_enemy(self, enemy: object | None = None) -> None:
        enemy = enemy or self.combat.enemy
        self.pending_display_enemy_hp = None
        self.display_enemy_name = enemy.name
        self.display_enemy_level = enemy.level
        self.display_enemy_is_boss = enemy.is_boss
        self.display_enemy_category = getattr(enemy, "category", "common")
        self.display_enemy_key = (
            "boss"
            if enemy.is_boss
            else getattr(
                enemy,
                "sprite_key",
                self.ENEMY_SPRITES.get(enemy.name, enemy.name.lower()),
            )
        )
        self.display_enemy_hp = enemy.current_hp
        self.display_enemy_max_hp = enemy.max_hp

    def _autosave(self) -> None:
        self.save_coordinator.save_now()
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _equip_item(self, item_id: str) -> None:
        item = self.hero.equip(item_id)
        if item is None:
            return
        self._append_log(f"{item.name} equipado.")
        self.save_coordinator.save_now()
        self._refresh()
        if (
            self.expanded_window is not None
            and self.expanded_window.winfo_exists()
        ):
            self.expanded_window.refresh(force_inventory=True)

    def _refresh(self) -> None:
        enemy = self.combat.enemy
        campaign = self.game_state.campaign

        self.header_stats.configure(
            text=f"NÍVEL {self.hero.level}\nOURO {self.hero.gold}"
        )
        status = (
            "CONCLUÍDO"
            if campaign.act_completed
            else f"{campaign.victories}/{campaign.target}"
        )
        self.map_header.configure(
            text=(
                f"ATO I  •  {campaign.map_number}/10  •  "
                f"{campaign.current_map}  [{status}]"
            )
        )

        hero_sprite = self.sprites.get("hero")
        self.hero_profile_sprite.configure(
            image=hero_sprite,
            text="" if hero_sprite else self.hero.name[0].upper(),
        )
        self._refresh_scene()

        self.hero_stats.configure(
            text=(
                f"{self.hero.name.upper()}\n"
                f"NÍVEL  {self.hero.level:<3}   OURO  {self.hero.gold}\n"
                f"HP     {self.hero.current_hp}/{self.hero.max_hp}\n"
                f"XP     {self.hero.xp}/{self.hero.xp_needed}\n"
                f"ATK    {self.hero.attack:<3}   DEF   {self.hero.defense}"
            )
        )
        self.build_summary.configure(
            text=(
                f"PODER {self.hero.power}  •  "
                f"EQUIPAMENTO {self.hero.equipment_power}"
            )
        )

        self.event_log.configure(text="\n".join(self.log_lines))
        if (
            self.expanded_window is not None
            and self.expanded_window.winfo_exists()
        ):
            self.expanded_window.refresh()

    def _refresh_scene(self) -> None:
        self._draw_environment()
        self._draw_motion_layer()
        self._draw_ambient_events()

        hero_frame = self.journey.hero_frame
        if self.journey.hero_hit_flash:
            hero_frame = "hit"
        hero_image = self.scene_hero_frames.get(
            hero_frame,
            self.scene_sprites.get("hero"),
        )
        if hero_image is not None:
            self.scene.itemconfigure(self.scene_hero, image=hero_image)

        enemy_image = self.scene_sprites.get(self.display_enemy_key)
        if enemy_image is not None:
            self.scene.itemconfigure(self.scene_enemy, image=enemy_image)

        hero_x = self.journey.hero_x
        enemy_x = self.journey.enemy_draw_x
        self.scene.coords(
            self.scene_hero,
            hero_x,
            90 + self.journey.hero_y_offset,
        )
        self.scene.coords(
            self.scene_enemy,
            enemy_x,
            90 + self.journey.enemy_y_offset,
        )
        self.scene.itemconfigure(
            self.scene_hero_name,
            text=f"{self.hero.name}  Nv.{self.hero.level}",
        )
        self.scene.coords(self.scene_hero_name, hero_x, 130)
        self._position_hero_hp(hero_x)

        show_enemy = (
            self.journey.enemy_visible
            and self.journey.enemy_opacity > 0.05
        )
        enemy_state = "normal" if show_enemy else "hidden"
        self.scene.itemconfigure(
            self.scene_enemy,
            state=(
                "hidden"
                if self.journey.enemy_hit_flash
                else enemy_state
            ),
        )
        for item in (
            self.scene_enemy_name,
            self.scene_enemy_hp_bg,
            self.scene_enemy_hp,
        ):
            self.scene.itemconfigure(item, state=enemy_state)

        if self.journey.phase == "explore":
            status = (
                f"RETOMANDO JORNADA  •  {self.journey.world_speed_percent}%"
                if self.journey.world_speed_percent < 100
                else (
                    "EXPLORANDO  •  "
                    f"{self.game_state.campaign.current_map.upper()}"
                )
            )
            self.scene.itemconfigure(
                self.scene_status,
                text=status,
            )
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        elif self.journey.phase == "encounter":
            self.scene.itemconfigure(
                self.scene_status,
                text=(
                    "ENCONTRO  •  "
                    f"DESACELERANDO {self.journey.world_speed_percent}%"
                ),
            )
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        elif self.journey.phase == "fight":
            self.scene.itemconfigure(self.scene_status, text="COMBATE AUTOMÁTICO")
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        else:
            self.scene.itemconfigure(self.scene_status, text="RECOMPENSA")
            self.scene.itemconfigure(
                self.scene_reward,
                text=self.journey.reward_text,
                state="normal",
            )

        enemy_label_x = max(216, min(270, enemy_x))
        self.scene.coords(self.scene_enemy_name, enemy_label_x, 130)
        self.scene.itemconfigure(
            self.scene_enemy_name,
            text=(
                f"{'CHEFE ' if self.display_enemy_is_boss else ''}"
                f"{'ELITE ' if self.display_enemy_category == 'elite' else ''}"
                f"{self.display_enemy_name}  Nv.{self.display_enemy_level}"
            ),
        )
        enemy_ratio = self._ratio(
            self.display_enemy_hp,
            self.display_enemy_max_hp,
        )
        self.scene.coords(
            self.scene_enemy_hp,
            216,
            140,
            216 + 108 * enemy_ratio,
            147,
        )

        self.scene.delete("fx")
        for projectile in self.journey.projectiles:
            tail_x = projectile.x - 23.0
            self.scene.create_line(
                tail_x,
                projectile.y,
                projectile.x,
                projectile.y,
                fill="#7b3f19",
                width=7,
                tags=("fx", "projectile"),
            )
            self.scene.create_line(
                tail_x,
                projectile.y,
                projectile.x,
                projectile.y,
                fill="#ffe7a3",
                width=3,
                arrow=tk.LAST,
                arrowshape=(9, 10, 4),
                tags=("fx", "projectile"),
            )
        for floater in self.journey.floaters:
            self.scene.create_text(
                floater.x,
                floater.y,
                text=floater.text,
                fill=floater.color,
                font=("Consolas", 12, "bold"),
                tags=("fx",),
            )
        self.scene.tag_raise("actor")
        self.scene.tag_raise("hud")
        self.scene.tag_raise("fx")

    def _position_hero_hp(self, center_x: float) -> None:
        left = max(6, min(228, center_x - 54))
        right = left + 108
        self.scene.coords(self.scene_hero_hp_bg, left, 140, right, 147)
        hero_ratio = self._ratio(self.hero.current_hp, self.hero.max_hp)
        self.scene.coords(
            self.scene_hero_hp,
            left,
            140,
            left + 108 * hero_ratio,
            147,
        )

    def _append_log(self, message: str) -> None:
        self.log_lines.append(message)

    @staticmethod
    def _ratio(value: int, maximum: int) -> float:
        if maximum <= 0:
            return 0.0
        return max(0.0, min(1.0, value / maximum))

    def _on_close(self) -> None:
        self.save_coordinator.save_now()
        if (
            self.expanded_window is not None
            and self.expanded_window.winfo_exists()
        ):
            self.expanded_window.destroy()
        self.destroy()
