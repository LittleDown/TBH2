from __future__ import annotations

from collections import deque

import customtkinter as ctk

from combat.combat import CombatEngine
from game_state import GameState
from maps.campaign import ACT_NAME, MAP_NAMES
from save.save_manager import SaveManager


class MainWindow(ctk.CTk):
    COMBAT_INTERVAL_MS = 800
    SAVE_INTERVAL_MS = 10_000
    RARITY_COLORS = {
        "Comum": "#777777",
        "Raro": "#3f78c5",
        "Épico": "#8f4dc0",
    }

    def __init__(self, state: GameState, save_manager: SaveManager) -> None:
        super().__init__()
        self.game_state = state
        self.hero = state.hero
        self.save_manager = save_manager
        self.combat = CombatEngine(state)
        self.log_lines: deque[str] = deque(maxlen=3)
        self.panel_frames: dict[str, ctk.CTkFrame] = {}
        self.nav_buttons: dict[str, ctk.CTkButton] = {}
        self.map_rows: list[ctk.CTkLabel] = []
        self.inventory_signature: tuple[tuple[str, bool], ...] = ()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("TBH2 - TaskBar Hero 2")
        self.resizable(False, False)
        self.configure(fg_color="#100f17")
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._position_as_companion()

        self._build_ui()
        initial_enemy = self.combat.enemy
        initial_message = (
            f"Chefe {initial_enemy.name} apareceu!"
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

    def _build_ui(self) -> None:
        self._build_header()
        self._build_combat_area()
        self._build_event_log()
        self._build_navigation()
        self._build_panels()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, height=54, fg_color="#201a2c", corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = ctk.CTkLabel(
            header,
            text="TBH2",
            font=ctk.CTkFont(family="Consolas", size=23, weight="bold"),
            text_color="#f3c969",
        )
        title.pack(side="left", padx=12)

        self.header_stats = ctk.CTkLabel(
            header,
            text="",
            justify="right",
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.header_stats.pack(side="right", padx=12)

        self.map_header = ctk.CTkLabel(
            self,
            text="",
            height=28,
            fg_color="#171420",
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.map_header.pack(fill="x")

    def _build_combat_area(self) -> None:
        combat_frame = ctk.CTkFrame(
            self, height=174, fg_color="#15131d", corner_radius=0
        )
        combat_frame.pack(fill="x", padx=8, pady=(6, 0))
        combat_frame.pack_propagate(False)
        combat_frame.grid_columnconfigure((0, 1), weight=1, uniform="combat")

        hero_card = self._entity_card(combat_frame, 0, "#244e46")
        self.hero_avatar = hero_card["avatar"]
        self.hero_name = hero_card["name"]
        self.hero_hp_text = hero_card["hp_text"]
        self.hero_hp_bar = hero_card["hp_bar"]

        enemy_card = self._entity_card(combat_frame, 1, "#592f42")
        self.enemy_avatar = enemy_card["avatar"]
        self.enemy_name = enemy_card["name"]
        self.enemy_hp_text = enemy_card["hp_text"]
        self.enemy_hp_bar = enemy_card["hp_bar"]

        versus = ctk.CTkLabel(
            combat_frame,
            text="VS",
            width=30,
            height=30,
            fg_color="#2b2338",
            corner_radius=15,
            font=ctk.CTkFont(family="Consolas", size=13, weight="bold"),
            text_color="#f3c969",
        )
        versus.place(relx=0.5, rely=0.44, anchor="center")

    def _entity_card(
        self, parent: ctk.CTkFrame, column: int, accent: str
    ) -> dict[str, ctk.CTkBaseClass]:
        card = ctk.CTkFrame(parent, fg_color="#211c2b", corner_radius=8)
        card.grid(
            row=0,
            column=column,
            padx=(6, 3) if column == 0 else (3, 6),
            pady=6,
            sticky="nsew",
        )

        avatar = ctk.CTkLabel(
            card,
            text="?",
            width=60,
            height=60,
            fg_color=accent,
            corner_radius=6,
            font=ctk.CTkFont(family="Consolas", size=31, weight="bold"),
        )
        avatar.pack(pady=(8, 3))

        name = ctk.CTkLabel(
            card,
            text="",
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        name.pack()

        hp_text = ctk.CTkLabel(card, text="", font=ctk.CTkFont(size=10))
        hp_text.pack()

        hp_bar = ctk.CTkProgressBar(
            card,
            width=130,
            height=9,
            progress_color="#c74755",
            fg_color="#3a303d",
        )
        hp_bar.pack(pady=(2, 6))
        return {
            "avatar": avatar,
            "name": name,
            "hp_text": hp_text,
            "hp_bar": hp_bar,
        }

    def _build_event_log(self) -> None:
        self.event_log = ctk.CTkLabel(
            self,
            text="",
            height=45,
            fg_color="#201a2c",
            corner_radius=6,
            justify="left",
            anchor="w",
            wraplength=320,
            font=ctk.CTkFont(size=10),
        )
        self.event_log.pack(fill="x", padx=8, pady=6)

    def _build_panels(self) -> None:
        container = ctk.CTkFrame(self, fg_color="#15131d", corner_radius=8)
        container.pack(fill="both", expand=True, padx=8)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.panel_frames["Hero"] = self._build_hero_panel(container)
        self.panel_frames["Inventory"] = self._build_inventory_panel(container)
        self.panel_frames["Map"] = self._build_map_panel(container)
        for frame in self.panel_frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def _build_hero_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color="#15131d", corner_radius=8)
        panel.grid_columnconfigure(0, weight=1)

        self.hero_stats = ctk.CTkLabel(
            panel,
            text="",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Consolas", size=12),
        )
        self.hero_stats.grid(row=0, column=0, padx=12, pady=(10, 5), sticky="ew")

        self.xp_bar = ctk.CTkProgressBar(
            panel, height=9, progress_color="#4a78c2", fg_color="#302b3a"
        )
        self.xp_bar.grid(row=1, column=0, padx=12, sticky="ew")

        strategy_label = ctk.CTkLabel(
            panel,
            text="Estratégia",
            font=ctk.CTkFont(size=11, weight="bold"),
        )
        strategy_label.grid(row=2, column=0, padx=12, pady=(8, 2), sticky="w")

        self.strategy_control = ctk.CTkSegmentedButton(
            panel,
            values=["Agressivo", "Balanceado", "Defensivo"],
            command=self._change_strategy,
            selected_color="#80531e",
            selected_hover_color="#996725",
            unselected_color="#2a2434",
            font=ctk.CTkFont(size=10),
        )
        self.strategy_control.grid(row=3, column=0, padx=12, sticky="ew")

        self.equipment_label = ctk.CTkLabel(
            panel,
            text="",
            justify="left",
            anchor="w",
            fg_color="#211c2b",
            corner_radius=6,
            font=ctk.CTkFont(size=11),
        )
        self.equipment_label.grid(
            row=4, column=0, padx=12, pady=(9, 10), ipadx=8, ipady=5, sticky="ew"
        )
        return panel

    def _build_inventory_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color="#15131d", corner_radius=8)
        self.inventory_frame = ctk.CTkScrollableFrame(
            panel,
            fg_color="#15131d",
            label_text="Inventário - clique para equipar",
            label_font=ctk.CTkFont(size=11, weight="bold"),
        )
        self.inventory_frame.pack(fill="both", expand=True, padx=4, pady=4)
        for column in range(4):
            self.inventory_frame.grid_columnconfigure(column, weight=1)
        return panel

    def _build_map_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color="#15131d", corner_radius=8)
        self.map_summary = ctk.CTkLabel(
            panel,
            text="",
            font=ctk.CTkFont(size=11, weight="bold"),
        )
        self.map_summary.pack(fill="x", padx=10, pady=(8, 2))

        self.map_progress_bar = ctk.CTkProgressBar(
            panel, height=9, progress_color="#b88335", fg_color="#302b3a"
        )
        self.map_progress_bar.pack(fill="x", padx=12, pady=(0, 6))

        map_list = ctk.CTkScrollableFrame(panel, fg_color="#15131d")
        map_list.pack(fill="both", expand=True, padx=5, pady=(0, 5))
        for index, map_name in enumerate(MAP_NAMES):
            row = ctk.CTkLabel(
                map_list,
                text=f"{index + 1:02d}. {map_name}",
                height=24,
                anchor="w",
                corner_radius=4,
                font=ctk.CTkFont(size=10),
            )
            row.pack(fill="x", pady=1)
            self.map_rows.append(row)
        return panel

    def _build_navigation(self) -> None:
        navigation = ctk.CTkFrame(
            self, height=48, fg_color="#201a2c", corner_radius=0
        )
        navigation.pack(side="bottom", fill="x", pady=(6, 0))
        navigation.pack_propagate(False)

        for panel_name in ("Hero", "Inventory", "Map"):
            button = ctk.CTkButton(
                navigation,
                text=panel_name,
                width=104,
                height=32,
                fg_color="#332a42",
                hover_color="#493b5d",
                command=lambda name=panel_name: self._show_panel(name),
            )
            button.pack(side="left", expand=True, padx=3, pady=8)
            self.nav_buttons[panel_name] = button

    def _show_panel(self, panel_name: str) -> None:
        self.panel_frames[panel_name].tkraise()
        for name, button in self.nav_buttons.items():
            button.configure(fg_color="#80531e" if name == panel_name else "#332a42")

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
        self._append_log(f"{item.name} equipado no slot {item.slot}.")
        self.save_manager.save(self.game_state)
        self._refresh()

    def _refresh(self) -> None:
        enemy = self.combat.enemy
        campaign = self.game_state.campaign

        self.header_stats.configure(
            text=f"Nv. {self.hero.level}   Ouro {self.hero.gold}"
        )
        status = "CONCLUÍDO" if campaign.act_completed else (
            f"{campaign.victories}/{campaign.target}"
        )
        self.map_header.configure(
            text=(
                f"Ato I - {campaign.map_number}/10  "
                f"{campaign.current_map}  [{status}]"
            )
        )

        self.hero_avatar.configure(text=self.hero.name[0].upper())
        self.hero_name.configure(text=f"{self.hero.name}  Nv.{self.hero.level}")
        self.hero_hp_text.configure(
            text=f"HP {self.hero.current_hp}/{self.hero.max_hp}"
        )
        self.hero_hp_bar.set(self._ratio(self.hero.current_hp, self.hero.max_hp))

        enemy_marker = "B" if enemy.is_boss else enemy.name[0].upper()
        self.enemy_avatar.configure(
            text=enemy_marker,
            fg_color="#7b263d" if enemy.is_boss else "#592f42",
        )
        enemy_prefix = "CHEFE " if enemy.is_boss else ""
        self.enemy_name.configure(text=f"{enemy_prefix}{enemy.name}  Nv.{enemy.level}")
        self.enemy_hp_text.configure(text=f"HP {enemy.current_hp}/{enemy.max_hp}")
        self.enemy_hp_bar.set(self._ratio(enemy.current_hp, enemy.max_hp))

        self.hero_stats.configure(
            text=(
                f"HP   {self.hero.current_hp:>3}/{self.hero.max_hp:<3}    "
                f"ATK {self.hero.attack:<3}  DEF {self.hero.defense:<3}\n"
                f"XP   {self.hero.xp:>3}/{self.hero.xp_needed:<3}    "
                f"Vitórias {self.hero.enemies_defeated}  Mortes {self.hero.deaths}"
            )
        )
        self.xp_bar.set(self._ratio(self.hero.xp, self.hero.xp_needed))
        self.strategy_control.set(self.hero.strategy)

        weapon = self.hero.equipment["weapon"]
        armor = self.hero.equipment["armor"]
        weapon_text = (
            f"{weapon.name} (P{weapon.power}, +{weapon.attack_bonus} ATK)"
            if weapon
            else "Nenhuma"
        )
        armor_text = (
            f"{armor.name} (P{armor.power}, +{armor.defense_bonus} DEF)"
            if armor
            else "Nenhuma"
        )
        self.equipment_label.configure(
            text=f"ARMA     {weapon_text}\nDEFESA   {armor_text}"
        )

        self.event_log.configure(text="\n".join(self.log_lines))
        self._refresh_inventory()
        self._refresh_map()

    def _refresh_inventory(self) -> None:
        signature = tuple(
            (item.item_id, self.hero.is_equipped(item))
            for item in self.hero.inventory
        )
        if signature == self.inventory_signature:
            return
        self.inventory_signature = signature

        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        if not self.hero.inventory:
            empty = ctk.CTkLabel(
                self.inventory_frame,
                text="Nenhum item encontrado ainda.",
                text_color="#8e8798",
            )
            empty.grid(row=0, column=0, columnspan=4, pady=35)
            return

        for index, item in enumerate(self.hero.inventory):
            equipped = self.hero.is_equipped(item)
            bonus = item.attack_bonus or item.defense_bonus
            slot = "ATK" if item.slot == "weapon" else "DEF"
            marker = "EQUIPADO\n" if equipped else ""
            name_words = item.name.split()
            display_name = (
                f"{name_words[0]}\n{' '.join(name_words[1:])}"
                if len(name_words) > 1
                else item.name
            )
            button = ctk.CTkButton(
                self.inventory_frame,
                text=(
                    f"{marker}{display_name}\n"
                    f"{item.rarity} P{item.power} +{bonus} {slot}"
                ),
                width=72,
                height=64,
                fg_color=(
                    "#80531e"
                    if equipped
                    else self.RARITY_COLORS.get(item.rarity, "#555555")
                ),
                hover_color="#9a6a2c" if equipped else "#575066",
                font=ctk.CTkFont(size=9, weight="bold"),
                command=lambda item_id=item.item_id: self._equip_item(item_id),
            )
            button.grid(row=index // 4, column=index % 4, padx=3, pady=3, sticky="nsew")

    def _refresh_map(self) -> None:
        campaign = self.game_state.campaign
        summary_status = (
            "Ato I concluído"
            if campaign.act_completed
            else f"{campaign.victories}/{campaign.target} vitórias"
        )
        self.map_summary.configure(text=f"{ACT_NAME} - {summary_status}")
        self.map_progress_bar.set(
            1.0
            if campaign.act_completed
            else self._ratio(campaign.victories, campaign.target)
        )

        for index, row in enumerate(self.map_rows):
            if index < campaign.map_index or campaign.act_completed:
                row.configure(
                    text=f"{index + 1:02d}. {MAP_NAMES[index]}  [OK]",
                    fg_color="#23483e",
                    text_color="#b7e2cc",
                )
            elif index == campaign.map_index:
                marker = "  [CHEFE]" if campaign.next_encounter_is_boss else "  [ATUAL]"
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
