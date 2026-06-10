from __future__ import annotations

from collections import deque
from pathlib import Path

import customtkinter as ctk
from PIL import Image

from combat.combat import CombatEngine
from game_state import GameState
from maps.campaign import ACT_NAME, MAP_NAMES
from save.save_manager import SaveManager


class MainWindow(ctk.CTk):
    COMBAT_INTERVAL_MS = 800
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

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("TBH2 - TaskBar Hero 2")
        self.resizable(False, False)
        self.configure(fg_color=self.COLORS["window"])
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._position_as_companion()
        self.sprites = self._load_sprites()

        self._build_ui()
        initial_enemy = self.combat.enemy
        initial_message = (
            f"Chefe {initial_enemy.name} surgiu no caminho!"
            if initial_enemy.is_boss
            else f"Um {initial_enemy.name} nível {initial_enemy.level} apareceu."
        )
        self._append_log(initial_message)
        self._show_panel("Hero")
        self._refresh()
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)
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
        combat_frame = ctk.CTkFrame(
            self,
            height=177,
            fg_color=self.COLORS["panel"],
            border_width=1,
            border_color="#302638",
            corner_radius=8,
        )
        combat_frame.pack(fill="x", padx=8, pady=(6, 0))
        combat_frame.pack_propagate(False)

        ctk.CTkLabel(
            combat_frame,
            text="ENCONTRO ATUAL",
            height=20,
            font=ctk.CTkFont(family="Consolas", size=9, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(fill="x")

        battle = ctk.CTkFrame(combat_frame, fg_color="transparent")
        battle.pack(fill="both", expand=True, padx=5, pady=(0, 5))
        battle.grid_columnconfigure((0, 1), weight=1, uniform="combat")
        battle.grid_rowconfigure(0, weight=1)

        hero_card = self._entity_card(battle, 0, "#183a35")
        self.hero_avatar = hero_card["avatar"]
        self.hero_name = hero_card["name"]
        self.hero_hp_text = hero_card["hp_text"]
        self.hero_hp_bar = hero_card["hp_bar"]

        enemy_card = self._entity_card(battle, 1, "#432536")
        self.enemy_avatar = enemy_card["avatar"]
        self.enemy_name = enemy_card["name"]
        self.enemy_hp_text = enemy_card["hp_text"]
        self.enemy_hp_bar = enemy_card["hp_bar"]

        versus_badge = ctk.CTkFrame(
            battle,
            width=29,
            height=29,
            fg_color="#2a2034",
            border_width=1,
            border_color=self.COLORS["gold_dark"],
            corner_radius=14,
        )
        versus_badge.place(relx=0.5, rely=0.43, anchor="center")
        versus_badge.pack_propagate(False)
        ctk.CTkLabel(
            versus_badge,
            text="VS",
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(fill="both", expand=True)

    def _entity_card(
        self, parent: ctk.CTkFrame, column: int, accent: str
    ) -> dict[str, ctk.CTkBaseClass]:
        card = ctk.CTkFrame(
            parent,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color=accent,
            corner_radius=7,
        )
        card.grid(
            row=0,
            column=column,
            padx=(1, 3) if column == 0 else (3, 1),
            sticky="nsew",
        )

        avatar = ctk.CTkLabel(card, text="", width=86, height=86)
        avatar.pack(pady=(2, 0))

        name = ctk.CTkLabel(
            card,
            text="",
            font=ctk.CTkFont(size=11, weight="bold"),
        )
        name.pack()

        hp_text = ctk.CTkLabel(
            card,
            text="",
            font=ctk.CTkFont(family="Consolas", size=9),
            text_color="#d9d2dd",
        )
        hp_text.pack()

        hp_bar = ctk.CTkProgressBar(
            card,
            width=132,
            height=8,
            progress_color=self.COLORS["hp"],
            fg_color="#3b303e",
        )
        hp_bar.pack(pady=(1, 5))
        return {
            "avatar": avatar,
            "name": name,
            "hp_text": hp_text,
            "hp_bar": hp_bar,
        }

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

    def _combat_tick(self) -> None:
        important_event = False
        for event in self.combat.tick():
            self._append_log(event.message)
            if event.kind in {
                "victory",
                "defeat",
                "level_up",
                "loot",
                "map_complete",
                "act_complete",
            }:
                important_event = True
        if important_event:
            self.save_manager.save(self.game_state)
        self._refresh()
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)

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
        self.hero_avatar.configure(
            image=hero_sprite,
            text="" if hero_sprite else self.hero.name[0].upper(),
        )
        self.hero_profile_sprite.configure(
            image=hero_sprite,
            text="" if hero_sprite else self.hero.name[0].upper(),
        )
        self.hero_name.configure(text=f"{self.hero.name}  Nv.{self.hero.level}")
        self.hero_hp_text.configure(
            text=f"HP {self.hero.current_hp}/{self.hero.max_hp}"
        )
        self.hero_hp_bar.set(self._ratio(self.hero.current_hp, self.hero.max_hp))

        enemy_key = (
            "boss"
            if enemy.is_boss
            else self.ENEMY_SPRITES.get(enemy.name, enemy.name.lower())
        )
        enemy_sprite = self.sprites.get(enemy_key)
        self.enemy_avatar.configure(
            image=enemy_sprite,
            text="" if enemy_sprite else enemy.name[0].upper(),
        )
        enemy_prefix = "CHEFE " if enemy.is_boss else ""
        self.enemy_name.configure(text=f"{enemy_prefix}{enemy.name}  Nv.{enemy.level}")
        self.enemy_hp_text.configure(text=f"HP {enemy.current_hp}/{enemy.max_hp}")
        self.enemy_hp_bar.set(self._ratio(enemy.current_hp, enemy.max_hp))

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
