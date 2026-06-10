from __future__ import annotations

from collections import deque
from pathlib import Path
from random import Random
import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from combat.combat import CombatEngine
from game_state import GameState
from maps.campaign import ACT_NAME, MAP_NAMES
from save.save_manager import SaveManager


class MainWindow(ctk.CTk):
    COMBAT_INTERVAL_MS = 800
    JOURNEY_FRAME_MS = 80
    ENCOUNTER_PAUSE_MS = 550
    REWARD_PAUSE_MS = 1_800
    SAVE_INTERVAL_MS = 10_000
    INVENTORY_CAPACITY = 20
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
    RARITY_COLORS = {
        "Comum": "#625e68",
        "Raro": "#315f99",
        "Épico": "#78449c",
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
        ("#6f8791", "#3f5b51", "#80694d", "bridge"),
        ("#77766e", "#4d5041", "#756b55", "ruins"),
        ("#89929a", "#56605d", "#777369", "fog"),
        ("#7e6c65", "#4d433e", "#76624d", "gate"),
        ("#514d58", "#36333c", "#62564e", "fortress"),
    )

    def __init__(self, state: GameState, save_manager: SaveManager) -> None:
        super().__init__()
        self.game_state = state
        self.hero = state.hero
        self.save_manager = save_manager
        self.combat = CombatEngine(state)
        self.log_lines: deque[str] = deque(maxlen=1)
        self.panel_frames: dict[str, ctk.CTkFrame] = {}
        self.nav_buttons: dict[str, ctk.CTkButton] = {}
        self.map_rows: list[ctk.CTkLabel] = []
        self.inventory_signature: tuple[tuple[str, bool], ...] | None = None
        self.inventory_detail_text = "Selecione um item para equipar."
        self.visual_rng = Random()
        self.journey_phase = "exploration"
        self.journey_ticks_remaining = 0
        self.hero_scene_x = 42
        self.hero_walk_frame = 0
        self.scene_map_index = -1
        self.scene_reward_text = ""

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("TBH2 - TaskBar Hero 2")
        self.resizable(False, False)
        self.configure(fg_color=self.COLORS["window"])
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._position_as_companion()
        self.sprites = self._load_sprites()

        self._build_ui()
        self._show_panel("Hero")
        self._start_exploration(initial=True)
        self.after(self.JOURNEY_FRAME_MS, self._journey_tick)
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _position_as_companion(self) -> None:
        width, height = 360, 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = max(0, screen_width - width - 18)
        y = max(0, screen_height - height - 70)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def _load_sprites(self) -> dict[str, ctk.CTkImage]:
        asset_dir = Path(__file__).resolve().parents[1] / "assets" / "sprites"
        sprites: dict[str, ctk.CTkImage] = {}
        self.scene_sprites: dict[str, ImageTk.PhotoImage] = {}
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
        return sprites

    def _build_ui(self) -> None:
        self._build_header()
        self._build_combat_area()
        self._build_last_action()
        self._build_navigation()
        self._build_panels()

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

        hero_image = self.scene_sprites.get("hero")
        self.scene_hero = self.scene.create_image(
            self.hero_scene_x,
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

    def _draw_fields(self) -> None:
        for x in (20, 58, 294, 326):
            self.scene.create_line(
                x, 79, x - 8, 108, fill="#c0a45c", width=2, tags=("environment",)
            )
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

    def _build_panels(self) -> None:
        container = ctk.CTkFrame(
            self,
            fg_color=self.COLORS["panel"],
            border_width=1,
            border_color="#2c2434",
            corner_radius=7,
        )
        container.pack(fill="both", expand=True, padx=8)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.panel_frames["Hero"] = self._build_hero_panel(container)
        self.panel_frames["Inventory"] = self._build_inventory_panel(container)
        self.panel_frames["Map"] = self._build_map_panel(container)
        for frame in self.panel_frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def _build_hero_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"], corner_radius=7)
        panel.grid_columnconfigure(0, weight=1)

        profile = ctk.CTkFrame(panel, fg_color=self.COLORS["panel_alt"], height=77)
        profile.grid(row=0, column=0, padx=7, pady=(7, 4), sticky="ew")
        profile.pack_propagate(False)
        self.hero_profile_sprite = ctk.CTkLabel(profile, text="", width=74, height=74)
        self.hero_profile_sprite.pack(side="left", padx=(5, 1))
        self.hero_stats = ctk.CTkLabel(
            profile,
            text="",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Consolas", size=10),
        )
        self.hero_stats.pack(side="left", fill="both", expand=True, padx=4, pady=4)

        ctk.CTkLabel(
            panel,
            text="EQUIPAMENTOS",
            height=16,
            font=ctk.CTkFont(family="Consolas", size=9, weight="bold"),
            text_color=self.COLORS["gold"],
        ).grid(row=1, column=0, padx=8, sticky="w")

        equipment = ctk.CTkFrame(panel, fg_color="transparent")
        equipment.grid(row=2, column=0, padx=6, sticky="ew")
        equipment.grid_columnconfigure((0, 1, 2), weight=1, uniform="equipment")
        self.weapon_slot = self._equipment_slot(equipment, 0, "ARMA")
        self.armor_slot = self._equipment_slot(equipment, 1, "ARMADURA")
        self.accessory_slot = self._equipment_slot(equipment, 2, "ACESSÓRIO")

        strategy_row = ctk.CTkFrame(panel, fg_color="transparent")
        strategy_row.grid(row=3, column=0, padx=7, pady=(5, 6), sticky="ew")
        ctk.CTkLabel(
            strategy_row,
            text="ESTRATÉGIA",
            width=67,
            font=ctk.CTkFont(family="Consolas", size=8, weight="bold"),
            text_color=self.COLORS["muted"],
        ).pack(side="left")
        self.strategy_control = ctk.CTkSegmentedButton(
            strategy_row,
            values=["Agressivo", "Balanceado", "Defensivo"],
            command=self._change_strategy,
            height=27,
            selected_color=self.COLORS["gold_dark"],
            selected_hover_color="#986822",
            unselected_color=self.COLORS["panel_light"],
            font=ctk.CTkFont(size=8),
        )
        self.strategy_control.pack(side="left", fill="x", expand=True)
        return panel

    def _equipment_slot(
        self, parent: ctk.CTkFrame, column: int, title: str
    ) -> ctk.CTkLabel:
        slot = ctk.CTkFrame(
            parent,
            height=58,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#4a3a55",
            corner_radius=5,
        )
        slot.grid(row=0, column=column, padx=2, sticky="ew")
        slot.pack_propagate(False)
        ctk.CTkLabel(
            slot,
            text=title,
            height=18,
            font=ctk.CTkFont(family="Consolas", size=8, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(fill="x")
        value = ctk.CTkLabel(
            slot,
            text="Vazio",
            wraplength=92,
            font=ctk.CTkFont(size=8),
            text_color="#d7cedc",
        )
        value.pack(fill="both", expand=True, padx=2, pady=(0, 2))
        return value

    def _build_inventory_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"], corner_radius=7)
        self.inventory_title = ctk.CTkLabel(
            panel,
            text="MOCHILA 0/20",
            height=20,
            font=ctk.CTkFont(family="Consolas", size=10, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.inventory_title.pack(fill="x", padx=7, pady=(5, 1))

        self.inventory_frame = ctk.CTkFrame(panel, fg_color="transparent")
        self.inventory_frame.pack(fill="x", padx=6)
        for column in range(5):
            self.inventory_frame.grid_columnconfigure(column, weight=1, uniform="bag")

        self.inventory_detail = ctk.CTkLabel(
            panel,
            text=self.inventory_detail_text,
            height=24,
            fg_color=self.COLORS["panel_alt"],
            corner_radius=5,
            wraplength=315,
            font=ctk.CTkFont(size=8),
            text_color="#d7cedc",
        )
        self.inventory_detail.pack(fill="x", padx=7, pady=(4, 6))
        return panel

    def _build_map_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"], corner_radius=7)
        self.map_summary = ctk.CTkLabel(
            panel,
            text="",
            font=ctk.CTkFont(family="Consolas", size=10, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.map_summary.pack(fill="x", padx=9, pady=(7, 2))

        self.map_progress_bar = ctk.CTkProgressBar(
            panel,
            height=8,
            progress_color=self.COLORS["gold"],
            fg_color="#30283a",
        )
        self.map_progress_bar.pack(fill="x", padx=11, pady=(0, 5))

        map_list = ctk.CTkScrollableFrame(panel, fg_color=self.COLORS["panel"])
        map_list.pack(fill="both", expand=True, padx=4, pady=(0, 4))
        for index, map_name in enumerate(MAP_NAMES):
            row = ctk.CTkLabel(
                map_list,
                text=f"{index + 1:02d}. {map_name}",
                height=22,
                anchor="w",
                corner_radius=4,
                font=ctk.CTkFont(size=9),
            )
            row.pack(fill="x", pady=1)
            self.map_rows.append(row)
        return panel

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

        for panel_name in ("Hero", "Inventory", "Map"):
            button = ctk.CTkButton(
                navigation,
                text=panel_name,
                width=104,
                height=32,
                fg_color="#30253e",
                hover_color="#49365b",
                font=ctk.CTkFont(size=10, weight="bold"),
                command=lambda name=panel_name: self._show_panel(name),
            )
            button.pack(side="left", expand=True, padx=3, pady=8)
            self.nav_buttons[panel_name] = button

    def _show_panel(self, panel_name: str) -> None:
        self.panel_frames[panel_name].tkraise()
        for name, button in self.nav_buttons.items():
            button.configure(
                fg_color=self.COLORS["gold_dark"]
                if name == panel_name
                else "#30253e"
            )

    def _start_exploration(self, initial: bool = False) -> None:
        self.journey_phase = "exploration"
        self.journey_ticks_remaining = self.visual_rng.randint(30, 48)
        self.hero_scene_x = 42 if initial else 28
        self.hero_walk_frame = 0
        self.scene_reward_text = ""
        action = (
            f"{self.hero.name} iniciou sua jornada por "
            f"{self.game_state.campaign.current_map}."
            if initial
            else f"{self.hero.name} retomou a caminhada."
        )
        self._append_log(action)
        self._refresh()

    def _journey_tick(self) -> None:
        if self.journey_phase == "exploration":
            self.hero_walk_frame += 1
            self.hero_scene_x += 3
            if self.hero_scene_x > 290:
                self.hero_scene_x = 28
            bob = -2 if self.hero_walk_frame % 4 < 2 else 0
            self.scene.coords(self.scene_hero, self.hero_scene_x, 90 + bob)
            self.scene.coords(
                self.scene_hero_name,
                max(72, min(270, self.hero_scene_x)),
                130,
            )
            self._position_hero_hp(self.hero_scene_x)
            self.journey_ticks_remaining -= 1
            if self.journey_ticks_remaining <= 0:
                self._begin_encounter()
        self.after(self.JOURNEY_FRAME_MS, self._journey_tick)

    def _begin_encounter(self) -> None:
        if self.journey_phase != "exploration":
            return
        self.journey_phase = "encounter"
        self.hero_scene_x = 76
        enemy = self.combat.enemy
        encounter_text = (
            f"Chefe {enemy.name} bloqueou a passagem!"
            if enemy.is_boss
            else f"{self.hero.name} encontrou {enemy.name}."
        )
        self._append_log(encounter_text)
        self._refresh()
        self.after(self.ENCOUNTER_PAUSE_MS, self._begin_combat)

    def _begin_combat(self) -> None:
        if self.journey_phase != "encounter":
            return
        self.journey_phase = "combat"
        self._append_log(f"Combate iniciado contra {self.combat.enemy.name}.")
        self._refresh()
        self.after(320, self._combat_tick)

    def _combat_tick(self) -> None:
        if self.journey_phase != "combat":
            return
        important_event = False
        events = self.combat.tick()
        for event in events:
            if event.kind in {
                "victory",
                "defeat",
                "level_up",
                "loot",
                "map_complete",
                "act_complete",
            }:
                important_event = True

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
        if important_event:
            self.save_manager.save(self.game_state)

        if victory_event is not None:
            loot_event = next(
                (
                    event
                    for event in events
                    if event.kind == "loot" and event.item is not None
                ),
                None,
            )
            self.scene_reward_text = victory_event.message
            if loot_event is not None:
                self.scene_reward_text += f"\nLoot: {loot_event.item.name}"
            self._append_log(self.scene_reward_text.replace("\n", "  •  "))
            self.journey_phase = "reward"
            self._refresh()
            self.after(self.REWARD_PAUSE_MS, self._start_exploration)
            return

        if defeat_event is not None:
            self.scene_reward_text = "O aventureiro caiu, mas retornará à estrada."
            self._append_log(defeat_event.message)
            self.journey_phase = "reward"
            self._refresh()
            self.after(self.REWARD_PAUSE_MS, self._start_exploration)
            return

        self._refresh()
        if attack_event is not None:
            self._animate_attack(attack_event.kind)
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)

    def _animate_attack(self, kind: str) -> None:
        if kind == "hero_attack":
            attacker = self.scene_hero
            target = self.scene_enemy
            delta = 10
        else:
            attacker = self.scene_enemy
            target = self.scene_hero
            delta = -10
        self.scene.move(attacker, delta, 0)
        self.scene.itemconfigure(target, state="hidden")
        self.after(80, lambda: self._restore_damage_target(target))
        self.after(150, lambda: self._restore_attacker(attacker, delta))

    def _restore_damage_target(self, target: int) -> None:
        if self.journey_phase == "combat":
            self.scene.itemconfigure(target, state="normal")

    def _restore_attacker(self, attacker: int, delta: int) -> None:
        if self.journey_phase == "combat":
            self.scene.move(attacker, -delta, 0)

    def _autosave(self) -> None:
        self.save_manager.save(self.game_state)
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _change_strategy(self, strategy: str) -> None:
        if self.hero.set_strategy(strategy):
            self._append_log(f"Estratégia alterada para {strategy}.")
            self.save_manager.save(self.game_state)
            self._refresh()

    def _equip_item(self, item_id: str) -> None:
        item = self.hero.equip(item_id)
        if item is None:
            return
        bonus = item.attack_bonus or item.defense_bonus
        bonus_name = "ATK" if item.slot == "weapon" else "DEF"
        self.inventory_detail_text = (
            f"{item.name} equipado | {item.rarity} | "
            f"Poder {item.power} | +{bonus} {bonus_name}"
        )
        self._append_log(f"{item.name} equipado.")
        self.save_manager.save(self.game_state)
        self._refresh()

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
                f"LEVEL  {self.hero.level:<3}   OURO  {self.hero.gold}\n"
                f"HP     {self.hero.current_hp}/{self.hero.max_hp}\n"
                f"XP     {self.hero.xp}/{self.hero.xp_needed}\n"
                f"ATK    {self.hero.attack:<3}   DEF   {self.hero.defense}"
            )
        )
        self.strategy_control.set(self.hero.strategy)

        weapon = self.hero.equipment["weapon"]
        armor = self.hero.equipment["armor"]
        accessory = self.hero.equipment["accessory"]
        self.weapon_slot.configure(
            text=f"{weapon.name}\nP{weapon.power}" if weapon else "Slot vazio"
        )
        self.armor_slot.configure(
            text=f"{armor.name}\nP{armor.power}" if armor else "Slot vazio"
        )
        self.accessory_slot.configure(
            text=f"{accessory.name}\nP{accessory.power}"
            if accessory
            else "Ainda não disponível",
            text_color="#d7cedc" if accessory else self.COLORS["muted"],
        )

        self.event_log.configure(text="\n".join(self.log_lines))
        self._refresh_inventory()
        self._refresh_map()

    def _refresh_scene(self) -> None:
        self._draw_environment()
        enemy = self.combat.enemy
        enemy_key = (
            "boss"
            if enemy.is_boss
            else self.ENEMY_SPRITES.get(enemy.name, enemy.name.lower())
        )
        enemy_image = self.scene_sprites.get(enemy_key)
        if enemy_image is not None:
            self.scene.itemconfigure(self.scene_enemy, image=enemy_image)

        enemy_ratio = self._ratio(enemy.current_hp, enemy.max_hp)
        self.scene.itemconfigure(
            self.scene_hero_name,
            text=f"{self.hero.name}  Nv.{self.hero.level}",
        )
        self._position_hero_hp(self.hero_scene_x)

        show_enemy = self.journey_phase in {"encounter", "combat"}
        enemy_state = "normal" if show_enemy else "hidden"
        for item in (
            self.scene_enemy,
            self.scene_enemy_name,
            self.scene_enemy_hp_bg,
            self.scene_enemy_hp,
        ):
            self.scene.itemconfigure(item, state=enemy_state)

        if self.journey_phase == "exploration":
            self.scene.itemconfigure(
                self.scene_status,
                text=f"EXPLORANDO  •  {self.game_state.campaign.current_map.upper()}",
            )
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        elif self.journey_phase == "encounter":
            self.hero_scene_x = 76
            self.scene.coords(self.scene_hero, self.hero_scene_x, 90)
            self.scene.coords(self.scene_hero_name, self.hero_scene_x, 130)
            self._position_hero_hp(self.hero_scene_x)
            self.scene.itemconfigure(self.scene_status, text="ENCONTRO!")
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        elif self.journey_phase == "combat":
            self.hero_scene_x = 76
            self.scene.coords(self.scene_hero, self.hero_scene_x, 90)
            self.scene.coords(self.scene_hero_name, self.hero_scene_x, 130)
            self._position_hero_hp(self.hero_scene_x)
            self.scene.itemconfigure(self.scene_status, text="COMBATE AUTOMÁTICO")
            self.scene.itemconfigure(self.scene_reward, state="hidden")
        else:
            self.hero_scene_x = 116
            self.scene.coords(self.scene_hero, self.hero_scene_x, 90)
            self.scene.coords(self.scene_hero_name, self.hero_scene_x, 130)
            self._position_hero_hp(self.hero_scene_x)
            self.scene.itemconfigure(self.scene_status, text="RECOMPENSA")
            self.scene.itemconfigure(
                self.scene_reward,
                text=self.scene_reward_text,
                state="normal",
            )

        self.scene.coords(self.scene_enemy, 270, 90)
        self.scene.coords(self.scene_enemy_name, 270, 130)
        self.scene.itemconfigure(
            self.scene_enemy_name,
            text=f"{'CHEFE ' if enemy.is_boss else ''}{enemy.name}  Nv.{enemy.level}",
        )
        self.scene.coords(
            self.scene_enemy_hp,
            216,
            140,
            216 + 108 * enemy_ratio,
            147,
        )
        self.scene.tag_raise("actor")
        self.scene.tag_raise("hud")

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

    def _refresh_inventory(self) -> None:
        visible_items = self.hero.inventory[-self.INVENTORY_CAPACITY :]
        signature = tuple(
            (item.item_id, self.hero.is_equipped(item)) for item in visible_items
        )
        if signature == self.inventory_signature:
            self.inventory_detail.configure(text=self.inventory_detail_text)
            return
        self.inventory_signature = signature

        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        item_count = len(self.hero.inventory)
        count_text = (
            f"{self.INVENTORY_CAPACITY}+"
            if item_count > self.INVENTORY_CAPACITY
            else str(item_count)
        )
        self.inventory_title.configure(
            text=f"MOCHILA {count_text}/{self.INVENTORY_CAPACITY}  •  GRID 5x4"
        )
        chest_image = self.sprites.get("loot_chest")

        for index in range(self.INVENTORY_CAPACITY):
            row, column = divmod(index, 5)
            if index < len(visible_items):
                item = visible_items[index]
                equipped = self.hero.is_equipped(item)
                slot_text = "ARMA" if item.slot == "weapon" else "DEF"
                button = ctk.CTkButton(
                    self.inventory_frame,
                    text=f"P{item.power}\n{slot_text}",
                    image=chest_image,
                    compound="left",
                    width=60,
                    height=35,
                    border_width=1,
                    border_color=(
                        self.COLORS["gold"]
                        if equipped
                        else self.RARITY_COLORS.get(item.rarity, "#625e68")
                    ),
                    fg_color=(
                        self.COLORS["gold_dark"]
                        if equipped
                        else self.RARITY_COLORS.get(item.rarity, "#625e68")
                    ),
                    hover_color="#91652a",
                    font=ctk.CTkFont(family="Consolas", size=7, weight="bold"),
                    command=lambda item_id=item.item_id: self._equip_item(item_id),
                )
            else:
                button = ctk.CTkButton(
                    self.inventory_frame,
                    text=f"{index + 1:02d}",
                    width=60,
                    height=35,
                    state="disabled",
                    border_width=1,
                    border_color="#332a3a",
                    fg_color="#1b1721",
                    text_color_disabled="#514858",
                    font=ctk.CTkFont(family="Consolas", size=8),
                )
            button.grid(row=row, column=column, padx=2, pady=1, sticky="nsew")

        self.inventory_detail.configure(text=self.inventory_detail_text)

    def _refresh_map(self) -> None:
        campaign = self.game_state.campaign
        summary_status = (
            "Ato I concluído"
            if campaign.act_completed
            else f"{campaign.victories}/{campaign.target} vitórias"
        )
        self.map_summary.configure(text=f"{ACT_NAME.upper()}  •  {summary_status}")
        self.map_progress_bar.set(
            1.0
            if campaign.act_completed
            else self._ratio(campaign.victories, campaign.target)
        )

        for index, row in enumerate(self.map_rows):
            if index < campaign.map_index or campaign.act_completed:
                row.configure(
                    text=f"{index + 1:02d}. {MAP_NAMES[index]}  [OK]",
                    fg_color=self.COLORS["success"],
                    text_color="#bde8d3",
                )
            elif index == campaign.map_index:
                marker = (
                    "  [CHEFE]" if campaign.next_encounter_is_boss else "  [ATUAL]"
                )
                row.configure(
                    text=f"{index + 1:02d}. {MAP_NAMES[index]}{marker}",
                    fg_color="#62431f",
                    text_color="#f3d79b",
                )
            else:
                row.configure(
                    text=f"{index + 1:02d}. {MAP_NAMES[index]}",
                    fg_color="transparent",
                    text_color="#77717f",
                )

    def _append_log(self, message: str) -> None:
        self.log_lines.append(message)

    @staticmethod
    def _ratio(value: int, maximum: int) -> float:
        if maximum <= 0:
            return 0.0
        return max(0.0, min(1.0, value / maximum))

    def _on_close(self) -> None:
        self.save_manager.save(self.game_state)
        self.destroy()
