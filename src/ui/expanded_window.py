from __future__ import annotations

from pathlib import Path
import tkinter as tk
from typing import Callable

import customtkinter as ctk
from PIL import Image

from game_state import GameState
from hero.classes import class_display_name
from items.items import Item
from maps.campaign import ACT_NAME
from maps.world import ACT_ONE_MAPS
from ui.class_visuals import resolve_visual_asset
from ui.presentation import (
    InventoryFilter,
    compare_item,
    current_map_summary,
    filter_inventory,
    map_status,
    next_objective,
)


class ExpandedWindow(ctk.CTkToplevel):
    WIDTH = 800
    HEIGHT = 600
    INVENTORY_PAGE_SIZE = 20
    OFFICIAL_SLOTS = (
        ("helmet", "Capacete"),
        ("amulet", "Amuleto"),
        ("weapon", "Arma"),
        ("offhand", "Mão Sec."),
        ("ring_1", "Anel 1"),
        ("chest", "Peitoral"),
        ("gloves", "Luvas"),
        ("belt", "Cinto"),
        ("boots", "Botas"),
        ("ring_2", "Anel 2"),
    )
    COLORS = {
        "window": "#0d0b12",
        "panel": "#17131f",
        "panel_alt": "#211a2b",
        "panel_light": "#2b2236",
        "gold": "#e0a640",
        "gold_dark": "#81551a",
        "text": "#f2edf5",
        "muted": "#9c91a5",
        "success": "#285746",
        "danger": "#8b3e43",
    }
    RARITY_COLORS = {
        "Comum": "#b9b3bf",
        "Raro": "#68a8ef",
        "Épico": "#c17be8",
    }

    def __init__(
        self,
        master: ctk.CTk,
        state: GameState,
        on_equip: Callable[[str], None],
    ) -> None:
        super().__init__(master)
        self.game_state = state
        self.hero = state.hero
        self.on_equip = on_equip
        self.active_panel = "Herói"
        self.panel_frames: dict[str, ctk.CTkFrame] = {}
        self.tab_buttons: dict[str, ctk.CTkButton] = {}
        self.slot_values: dict[str, ctk.CTkLabel] = {}
        self.map_rows: list[ctk.CTkLabel] = []
        self.selected_filter: InventoryFilter = "Todos"
        self.selected_item_id: str | None = None
        self.inventory_page = 0
        self.inventory_signature: tuple[object, ...] | None = None
        self.inventory_hitboxes: list[
            tuple[float, float, float, float, str]
        ] = []
        self._hero_image: ctk.CTkImage | None = None

        self.title("TBH2 - Gerenciamento")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.minsize(720, 560)
        self.configure(fg_color=self.COLORS["window"])
        self.protocol("WM_DELETE_WINDOW", self.hide)
        self.transient(master)
        self._position_near_master()
        self._load_images()
        self._build_ui()
        self.show_panel("Herói")
        self.refresh()

    def _position_near_master(self) -> None:
        self.update_idletasks()
        master_x = self.master.winfo_x()
        master_y = self.master.winfo_y()
        left_x = master_x - self.WIDTH - 12
        x = left_x if left_x >= 0 else max(0, master_x - 220)
        screen_height = self.winfo_screenheight()
        y = max(0, min(master_y, screen_height - self.HEIGHT - 40))
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

    def _load_images(self) -> None:
        asset_root = Path(__file__).resolve().parents[1] / "assets"
        path = resolve_visual_asset(
            asset_root,
            self.hero.class_id,
            "front",
        )
        if path is None:
            return
        with Image.open(path) as source:
            image = source.convert("RGBA").copy()
        image.thumbnail((230, 310), Image.Resampling.LANCZOS)
        self._hero_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(image.width, image.height),
        )

    def _build_ui(self) -> None:
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build_tabs()
        content = ctk.CTkFrame(
            self,
            fg_color=self.COLORS["panel"],
            border_width=1,
            border_color="#4a3a32",
            corner_radius=0,
        )
        content.grid(row=1, column=0, padx=12, pady=(0, 12), sticky="nsew")
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        self.panel_frames["Herói"] = self._build_hero_panel(content)
        self.panel_frames["Mochila"] = self._build_inventory_panel(content)
        self.panel_frames["Mapa"] = self._build_map_panel(content)
        for frame in self.panel_frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def _build_tabs(self) -> None:
        tabs = ctk.CTkFrame(
            self,
            height=54,
            fg_color="#151119",
            border_width=1,
            border_color="#4a3a32",
            corner_radius=0,
        )
        tabs.grid(row=0, column=0, padx=12, pady=(12, 0), sticky="ew")
        tabs.grid_columnconfigure((0, 1, 2), weight=1, uniform="tabs")
        tabs.grid_columnconfigure(3, weight=0)

        for column, panel_name in enumerate(("Herói", "Mochila", "Mapa")):
            button = ctk.CTkButton(
                tabs,
                text=panel_name.upper(),
                height=42,
                corner_radius=0,
                fg_color="#221b25",
                hover_color="#3c2d3e",
                border_width=1,
                border_color="#4a3a32",
                font=ctk.CTkFont(
                    family="Georgia",
                    size=15,
                    weight="bold",
                ),
                command=lambda name=panel_name: self.show_panel(name),
            )
            button.grid(row=0, column=column, padx=(0, 1), sticky="ew")
            self.tab_buttons[panel_name] = button

        ctk.CTkButton(
            tabs,
            text="✕",
            width=46,
            height=42,
            corner_radius=0,
            fg_color="#2b2428",
            hover_color="#5b3134",
            border_width=1,
            border_color="#4a3a32",
            command=self.hide,
        ).grid(row=0, column=3, sticky="e")

    def _build_hero_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"])
        panel.grid_rowconfigure(0, weight=1)
        panel.grid_columnconfigure(0, weight=1, minsize=455)
        panel.grid_columnconfigure(1, weight=0, minsize=285)

        equipment_area = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        equipment_area.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=10,
            sticky="nsew",
        )
        equipment_area.grid_rowconfigure(1, weight=1)
        equipment_area.grid_columnconfigure(1, weight=1)

        self.hero_title = ctk.CTkLabel(
            equipment_area,
            text="",
            font=ctk.CTkFont(family="Georgia", size=18, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.hero_title.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(12, 4),
        )

        left_slots = ctk.CTkFrame(equipment_area, fg_color="transparent")
        left_slots.grid(row=1, column=0, padx=8, pady=4, sticky="ns")
        center = ctk.CTkFrame(
            equipment_area,
            fg_color="#141116",
            border_width=1,
            border_color="#4a3a32",
        )
        center.grid(row=1, column=1, padx=5, pady=4, sticky="nsew")
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(0, weight=1)
        right_slots = ctk.CTkFrame(equipment_area, fg_color="transparent")
        right_slots.grid(row=1, column=2, padx=8, pady=4, sticky="ns")

        self.hero_art = ctk.CTkLabel(
            center,
            text=class_display_name(self.hero.class_id).upper(),
            image=self._hero_image,
            compound="top",
            font=ctk.CTkFont(family="Georgia", size=12, weight="bold"),
            text_color="#d8c9df",
        )
        self.hero_art.grid(row=0, column=0, sticky="nsew")

        for index, (slot_id, title) in enumerate(self.OFFICIAL_SLOTS[:5]):
            self.slot_values[slot_id] = self._equipment_slot(
                left_slots,
                index,
                title,
            )
        for index, (slot_id, title) in enumerate(self.OFFICIAL_SLOTS[5:]):
            self.slot_values[slot_id] = self._equipment_slot(
                right_slots,
                index,
                title,
            )

        self.hero_power = ctk.CTkLabel(
            equipment_area,
            text="",
            height=36,
            fg_color=self.COLORS["panel_light"],
            font=ctk.CTkFont(family="Consolas", size=12, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.hero_power.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=9,
            pady=(4, 10),
            sticky="ew",
        )

        details = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        details.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=10,
            sticky="nsew",
        )
        details.grid_propagate(False)

        ctk.CTkLabel(
            details,
            text="ATRIBUTOS",
            font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(fill="x", padx=16, pady=(18, 10))
        self.attribute_text = ctk.CTkLabel(
            details,
            text="",
            justify="left",
            anchor="nw",
            font=ctk.CTkFont(family="Consolas", size=13),
        )
        self.attribute_text.pack(fill="x", padx=20, pady=4)

        ctk.CTkLabel(
            details,
            text="ATRIBUTOS FUTUROS",
            font=ctk.CTkFont(family="Consolas", size=10, weight="bold"),
            text_color=self.COLORS["muted"],
        ).pack(fill="x", padx=20, pady=(20, 4))
        ctk.CTkLabel(
            details,
            text=(
                "STR  Indisponível\n"
                "DEX  Indisponível\n"
                "INT  Indisponível\n"
                "CON  Indisponível\n\n"
                "Atributos primários e habilidades\n"
                "serão integrados em versões futuras."
            ),
            justify="left",
            anchor="nw",
            text_color=self.COLORS["muted"],
            font=ctk.CTkFont(family="Consolas", size=11),
        ).pack(fill="x", padx=20, pady=4)
        return panel

    def _equipment_slot(
        self,
        parent: ctk.CTkFrame,
        row: int,
        title: str,
    ) -> ctk.CTkLabel:
        frame = ctk.CTkFrame(
            parent,
            width=92,
            height=66,
            fg_color="#18141b",
            border_width=1,
            border_color="#534553",
            corner_radius=4,
        )
        frame.grid(row=row, column=0, pady=3, sticky="ew")
        frame.grid_propagate(False)
        ctk.CTkLabel(
            frame,
            text=title.upper(),
            height=19,
            font=ctk.CTkFont(family="Consolas", size=8, weight="bold"),
            text_color=self.COLORS["gold"],
        ).pack(fill="x")
        value = ctk.CTkLabel(
            frame,
            text="Indisponível",
            wraplength=84,
            font=ctk.CTkFont(size=8),
            text_color=self.COLORS["muted"],
        )
        value.pack(fill="both", expand=True, padx=2, pady=(0, 3))
        return value

    def _build_inventory_panel(
        self,
        parent: ctk.CTkFrame,
    ) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"])
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1, minsize=440)
        panel.grid_columnconfigure(1, weight=0, minsize=300)

        filters = ctk.CTkFrame(panel, fg_color="#151119", height=44)
        filters.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=(10, 5),
            sticky="ew",
        )
        self.filter_buttons: dict[str, ctk.CTkButton] = {}
        for filter_name in ("Todos", "Armas", "Armaduras", "Acessórios"):
            button = ctk.CTkButton(
                filters,
                text=filter_name,
                width=96,
                height=30,
                fg_color="#30253e",
                hover_color="#49365b",
                command=lambda name=filter_name: self._set_inventory_filter(name),
            )
            button.pack(side="left", padx=4, pady=7)
            self.filter_buttons[filter_name] = button
        self.inventory_count = ctk.CTkLabel(
            filters,
            text="",
            font=ctk.CTkFont(family="Consolas", size=10),
            text_color=self.COLORS["muted"],
        )
        self.inventory_count.pack(side="right", padx=12)
        self.next_page_button = ctk.CTkButton(
            filters,
            text="›",
            width=30,
            height=28,
            fg_color="#30253e",
            hover_color="#49365b",
            command=lambda: self._change_inventory_page(1),
        )
        self.next_page_button.pack(side="right", padx=(2, 4), pady=7)
        self.previous_page_button = ctk.CTkButton(
            filters,
            text="‹",
            width=30,
            height=28,
            fg_color="#30253e",
            hover_color="#49365b",
            command=lambda: self._change_inventory_page(-1),
        )
        self.previous_page_button.pack(side="right", padx=2, pady=7)

        inventory_container = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        inventory_container.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=(5, 10),
            sticky="nsew",
        )
        ctk.CTkLabel(
            inventory_container,
            text="ITENS",
            height=34,
            font=ctk.CTkFont(
                family="Consolas",
                size=11,
                weight="bold",
            ),
            text_color=self.COLORS["gold"],
        ).pack(fill="x", padx=6, pady=(2, 0))
        canvas_area = ctk.CTkFrame(
            inventory_container,
            fg_color="transparent",
        )
        canvas_area.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        self.inventory_canvas = tk.Canvas(
            canvas_area,
            background=self.COLORS["panel_alt"],
            highlightthickness=0,
            bd=0,
        )
        inventory_scrollbar = ctk.CTkScrollbar(
            canvas_area,
            width=12,
            command=self.inventory_canvas.yview,
        )
        self.inventory_canvas.configure(
            yscrollcommand=inventory_scrollbar.set
        )
        self.inventory_canvas.pack(side="left", fill="both", expand=True)
        inventory_scrollbar.pack(side="right", fill="y")
        self.inventory_canvas.bind(
            "<Button-1>",
            self._on_inventory_canvas_click,
        )
        self.inventory_canvas.bind(
            "<MouseWheel>",
            self._on_inventory_mousewheel,
        )

        detail = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        detail.grid(
            row=1,
            column=1,
            padx=(5, 10),
            pady=(5, 10),
            sticky="nsew",
        )
        detail.grid_propagate(False)
        self.item_name = ctk.CTkLabel(
            detail,
            text="Selecione um item",
            wraplength=265,
            font=ctk.CTkFont(family="Georgia", size=17, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.item_name.pack(fill="x", padx=14, pady=(18, 8))
        self.item_details = ctk.CTkLabel(
            detail,
            text="",
            justify="left",
            anchor="nw",
            font=ctk.CTkFont(family="Consolas", size=12),
        )
        self.item_details.pack(fill="x", padx=18, pady=6)
        self.comparison = ctk.CTkLabel(
            detail,
            text="",
            justify="left",
            anchor="nw",
            fg_color=self.COLORS["panel_light"],
            corner_radius=6,
            font=ctk.CTkFont(family="Consolas", size=12, weight="bold"),
        )
        self.comparison.pack(fill="x", padx=14, pady=12)
        self.equip_button = ctk.CTkButton(
            detail,
            text="EQUIPAR",
            height=38,
            fg_color=self.COLORS["gold_dark"],
            hover_color="#a26b22",
            command=self._equip_selected,
        )
        self.equip_button.pack(fill="x", padx=14, pady=(4, 8))
        future_actions = ctk.CTkFrame(detail, fg_color="transparent")
        future_actions.pack(fill="x", padx=10)
        for text in ("Favoritar", "Bloquear", "Vender"):
            ctk.CTkButton(
                future_actions,
                text=text,
                width=78,
                height=30,
                state="disabled",
                fg_color="#2a252d",
            ).pack(side="left", expand=True, fill="x", padx=3)
        ctk.CTkLabel(
            detail,
            text="Ações adicionais serão liberadas em versões futuras.",
            text_color=self.COLORS["muted"],
            font=ctk.CTkFont(size=9),
        ).pack(fill="x", padx=12, pady=10)
        return panel

    def _build_map_panel(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        panel = ctk.CTkFrame(parent, fg_color=self.COLORS["panel"])
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1, minsize=440)
        panel.grid_columnconfigure(1, weight=0, minsize=300)

        header = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        header.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=(10, 5),
            sticky="ew",
        )
        self.map_title = ctk.CTkLabel(
            header,
            text="",
            anchor="w",
            font=ctk.CTkFont(family="Georgia", size=17, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.map_title.pack(fill="x", padx=14, pady=(10, 2))
        self.map_progress = ctk.CTkProgressBar(
            header,
            height=9,
            progress_color=self.COLORS["gold"],
            fg_color="#30283a",
        )
        self.map_progress.pack(fill="x", padx=14, pady=(2, 10))

        map_list = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        map_list.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=(5, 10),
            sticky="nsew",
        )
        ctk.CTkLabel(
            map_list,
            text="MAPAS DO ATO I",
            height=34,
            fg_color="#323233",
            corner_radius=5,
            font=ctk.CTkFont(
                family="Consolas",
                size=11,
                weight="bold",
            ),
            text_color=self.COLORS["gold"],
        ).pack(fill="x", padx=6, pady=(6, 3))
        for index, definition in enumerate(ACT_ONE_MAPS):
            row = ctk.CTkLabel(
                map_list,
                text=f"{index + 1:02d}. {definition.name}",
                height=34,
                anchor="w",
                corner_radius=5,
                font=ctk.CTkFont(size=11),
            )
            row.pack(fill="x", padx=6, pady=2)
            self.map_rows.append(row)

        detail = ctk.CTkFrame(
            panel,
            fg_color=self.COLORS["panel_alt"],
            border_width=1,
            border_color="#443747",
        )
        detail.grid(
            row=1,
            column=1,
            padx=(5, 10),
            pady=(5, 10),
            sticky="nsew",
        )
        detail.grid_propagate(False)
        self.current_map_title = ctk.CTkLabel(
            detail,
            text="",
            wraplength=270,
            font=ctk.CTkFont(family="Georgia", size=17, weight="bold"),
            text_color=self.COLORS["gold"],
        )
        self.current_map_title.pack(fill="x", padx=14, pady=(20, 8))
        self.current_map_detail = ctk.CTkLabel(
            detail,
            text="",
            justify="left",
            anchor="nw",
            font=ctk.CTkFont(family="Consolas", size=12),
        )
        self.current_map_detail.pack(fill="x", padx=18, pady=6)
        self.next_objective_label = ctk.CTkLabel(
            detail,
            text="",
            wraplength=270,
            justify="left",
            fg_color=self.COLORS["panel_light"],
            corner_radius=6,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#c8e5d1",
        )
        self.next_objective_label.pack(fill="x", padx=14, pady=14)
        ctk.CTkButton(
            detail,
            text="IR PARA MAPA",
            height=36,
            state="disabled",
            fg_color="#2a252d",
        ).pack(fill="x", padx=14, pady=(8, 5))
        self.free_farm_button = ctk.CTkButton(
            detail,
            text="FREE FARM · EM PREPARAÇÃO",
            height=36,
            state="disabled",
            fg_color="#2a252d",
        )
        self.free_farm_button.pack(fill="x", padx=14, pady=5)
        return panel

    def show(self, panel_name: str = "Herói") -> None:
        self.deiconify()
        self.lift()
        self.show_panel(panel_name)
        self.refresh(force_inventory=True)
        self.focus_force()

    def hide(self) -> None:
        self.withdraw()

    def show_panel(self, panel_name: str) -> None:
        if panel_name not in self.panel_frames:
            return
        self.active_panel = panel_name
        self.panel_frames[panel_name].tkraise()
        for name, button in self.tab_buttons.items():
            button.configure(
                fg_color=(
                    self.COLORS["gold_dark"]
                    if name == panel_name
                    else "#221b25"
                ),
                text_color=(
                    "#fff1cf"
                    if name == panel_name
                    else self.COLORS["text"]
                ),
            )
        self.refresh(force_inventory=panel_name == "Mochila")

    def refresh(self, force_inventory: bool = False) -> None:
        if not self.winfo_exists():
            return
        self._refresh_hero()
        self._refresh_inventory(force=force_inventory)
        self._refresh_map()

    def _refresh_hero(self) -> None:
        hero = self.hero
        self.hero_art.configure(
            text=class_display_name(hero.class_id).upper()
        )
        self.hero_title.configure(
            text=(
                f"{hero.name.upper()} · "
                f"{class_display_name(hero.class_id).upper()} · "
                f"NÍVEL {hero.level}"
            )
        )
        self.hero_power.configure(
            text=f"PODER {hero.power}  ·  BUILD SCORE {hero.build_score}"
        )
        self.attribute_text.configure(
            text=(
                f"HP         {hero.current_hp}/{hero.max_hp}\n"
                f"XP         {hero.xp}/{hero.xp_needed}\n"
                f"ATAQUE     {hero.attack}\n"
                f"DEFESA     {hero.defense}\n"
                f"OURO       {hero.gold}\n"
                f"INIMIGOS   {hero.enemies_defeated}\n"
                f"CHEFES     {hero.bosses_defeated}"
            )
        )

        slot_items = {
            "weapon": hero.equipment.get("weapon"),
            "chest": hero.equipment.get("armor"),
            "amulet": hero.equipment.get("accessory"),
        }
        for slot_id, label in self.slot_values.items():
            item = slot_items.get(slot_id)
            if item is None:
                label.configure(
                    text=(
                        "Vazio"
                        if slot_id in slot_items
                        else "Indisponível"
                    ),
                    text_color=self.COLORS["muted"],
                )
                continue
            label.configure(
                text=f"{item.name}\nP{item.power}",
                text_color=self.RARITY_COLORS.get(
                    item.rarity,
                    self.COLORS["text"],
                ),
            )

    def _set_inventory_filter(self, filter_name: str) -> None:
        self.selected_filter = filter_name  # type: ignore[assignment]
        self.inventory_page = 0
        self.inventory_signature = None
        self._refresh_inventory(force=True)

    def _change_inventory_page(self, delta: int) -> None:
        self.inventory_page = max(0, self.inventory_page + delta)
        self.inventory_signature = None
        self._refresh_inventory(force=True)

    def _inventory_state_signature(self) -> tuple[object, ...]:
        return (
            self.selected_filter,
            self.inventory_page,
            tuple(
                (
                    item.item_id,
                    item.power,
                    self.hero.is_equipped(item),
                )
                for item in self.hero.inventory
            ),
        )

    def _refresh_inventory(self, force: bool = False) -> None:
        signature = self._inventory_state_signature()
        if not force and signature == self.inventory_signature:
            self._refresh_item_detail()
            return
        self.inventory_signature = signature

        for name, button in self.filter_buttons.items():
            button.configure(
                fg_color=(
                    self.COLORS["gold_dark"]
                    if name == self.selected_filter
                    else "#30253e"
                )
            )
        self.inventory_canvas.delete("all")
        self.inventory_hitboxes.clear()

        items = filter_inventory(
            self.hero.inventory,
            self.selected_filter,
        )
        ordered_items = list(reversed(items))
        page_count = max(
            1,
            (
                len(ordered_items)
                + self.INVENTORY_PAGE_SIZE
                - 1
            )
            // self.INVENTORY_PAGE_SIZE,
        )
        self.inventory_page = min(self.inventory_page, page_count - 1)
        page_start = self.inventory_page * self.INVENTORY_PAGE_SIZE
        page_items = ordered_items[
            page_start : page_start + self.INVENTORY_PAGE_SIZE
        ]
        self.inventory_count.configure(
            text=(
                f"{len(items)} itens · "
                f"Página {self.inventory_page + 1}/{page_count}"
            )
        )
        self.previous_page_button.configure(
            state="normal" if self.inventory_page > 0 else "disabled"
        )
        self.next_page_button.configure(
            state=(
                "normal"
                if self.inventory_page < page_count - 1
                else "disabled"
            )
        )
        if (
            self.selected_item_id is None
            or not any(
                item.item_id == self.selected_item_id
                for item in page_items
            )
        ):
            self.selected_item_id = (
                page_items[0].item_id if page_items else None
            )

        canvas_width = max(390, self.inventory_canvas.winfo_width())
        columns = 4
        gap = 6
        card_width = (canvas_width - gap * (columns + 1)) / columns
        card_height = 66
        for index, item in enumerate(page_items):
            row, column = divmod(index, 4)
            equipped = self.hero.is_equipped(item)
            x1 = gap + column * (card_width + gap)
            y1 = gap + row * (card_height + gap)
            x2 = x1 + card_width
            y2 = y1 + card_height
            selected = item.item_id == self.selected_item_id
            outline = (
                self.COLORS["gold"]
                if equipped or selected
                else self.RARITY_COLORS.get(item.rarity, "#625e68")
            )
            self.inventory_canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="#4e351b" if equipped else "#28222d",
                outline=outline,
                width=2 if equipped or selected else 1,
            )
            self.inventory_canvas.create_text(
                (x1 + x2) / 2,
                y1 + 22,
                text=item.name,
                fill=self.RARITY_COLORS.get(
                    item.rarity,
                    self.COLORS["text"],
                ),
                width=max(60, card_width - 10),
                justify="center",
                font=("Segoe UI", 8, "bold"),
            )
            self.inventory_canvas.create_text(
                (x1 + x2) / 2,
                y1 + 49,
                text=(
                    f"Poder {item.power}"
                    f"{' · EM USO' if equipped else ''}"
                ),
                fill="#f3d79b" if equipped else "#b9b3bf",
                font=("Consolas", 8, "bold"),
            )
            self.inventory_hitboxes.append(
                (x1, y1, x2, y2, item.item_id)
            )
        rows = max(
            1,
            (
                len(page_items)
                + columns
                - 1
            )
            // columns,
        )
        self.inventory_canvas.configure(
            scrollregion=(
                0,
                0,
                canvas_width,
                gap + rows * (card_height + gap),
            )
        )
        self.inventory_canvas.yview_moveto(0)
        self._refresh_item_detail()

    def _on_inventory_canvas_click(self, event: tk.Event) -> None:
        x = self.inventory_canvas.canvasx(event.x)
        y = self.inventory_canvas.canvasy(event.y)
        for x1, y1, x2, y2, item_id in self.inventory_hitboxes:
            if x1 <= x <= x2 and y1 <= y <= y2:
                self._select_item(item_id)
                self.inventory_signature = None
                self._refresh_inventory(force=True)
                return

    def _on_inventory_mousewheel(self, event: tk.Event) -> None:
        delta = -1 if event.delta > 0 else 1
        self.inventory_canvas.yview_scroll(delta, "units")

    def _select_item(self, item_id: str) -> None:
        self.selected_item_id = item_id
        self._refresh_item_detail()

    def _selected_item(self) -> Item | None:
        return next(
            (
                item
                for item in self.hero.inventory
                if item.item_id == self.selected_item_id
            ),
            None,
        )

    def _refresh_item_detail(self) -> None:
        item = self._selected_item()
        if item is None:
            self.item_name.configure(
                text="Mochila vazia",
                text_color=self.COLORS["muted"],
            )
            self.item_details.configure(text="Nenhum item neste filtro.")
            self.comparison.configure(text="")
            self.equip_button.configure(state="disabled")
            return

        equipped = self.hero.equipment.get(item.slot)
        comparison = compare_item(item, equipped)
        slot_name = {
            "weapon": "Arma",
            "armor": "Armadura",
            "accessory": "Acessório",
        }[item.slot]
        bonus_lines = []
        if item.attack_bonus:
            bonus_lines.append(f"ATK        +{item.attack_bonus}")
        if item.defense_bonus:
            bonus_lines.append(f"DEF        +{item.defense_bonus}")
        if not bonus_lines:
            bonus_lines.append("Bônus      Em preparação")

        self.item_name.configure(
            text=item.name,
            text_color=self.RARITY_COLORS.get(
                item.rarity,
                self.COLORS["text"],
            ),
        )
        self.item_details.configure(
            text=(
                f"TIPO       {slot_name}\n"
                f"RARIDADE   {item.rarity}\n"
                f"POWER      {item.power}\n"
                f"BUILD      {item.build_score}\n"
                + "\n".join(bonus_lines)
            )
        )
        current_name = equipped.name if equipped else "Slot vazio"
        delta_color = (
            "#a7e0b8"
            if comparison.power_delta > 0
            else (
                "#e1b3b3"
                if comparison.power_delta < 0
                else self.COLORS["muted"]
            )
        )
        self.comparison.configure(
            text=(
                f"COMPARAÇÃO\n"
                f"Em uso: {current_name}\n"
                f"Power: {comparison.power_delta:+d}\n"
                f"ATK: {comparison.attack_delta:+d}\n"
                f"DEF: {comparison.defense_delta:+d}"
            ),
            text_color=delta_color,
        )
        self.equip_button.configure(
            text="EQUIPADO" if comparison.is_equipped else "EQUIPAR",
            state="disabled" if comparison.is_equipped else "normal",
        )

    def _equip_selected(self) -> None:
        item = self._selected_item()
        if item is None:
            return
        self.on_equip(item.item_id)
        self.inventory_signature = None
        self.refresh(force_inventory=True)

    def _refresh_map(self) -> None:
        campaign = self.game_state.campaign
        difficulty_name = campaign.current_difficulty_id.title()
        self.map_title.configure(
            text=(
                f"ATO I · {ACT_NAME.upper()}  |  "
                f"DIFICULDADE: {difficulty_name}"
            )
        )
        self.map_progress.set(
            1.0
            if campaign.act_completed
            else (
                (
                    campaign.map_index
                    + campaign.victories / max(1, campaign.target)
                )
                / len(ACT_ONE_MAPS)
            )
        )

        status_text = {
            "completed": "✓",
            "current": "●",
            "locked": "🔒",
        }
        status_color = {
            "completed": (self.COLORS["success"], "#bde8d3"),
            "current": ("#62431f", "#f3d79b"),
            "locked": ("transparent", "#77717f"),
        }
        for index, row in enumerate(self.map_rows):
            status = map_status(campaign, index)
            background, text_color = status_color[status]
            boss_marker = " · CHEFE" if ACT_ONE_MAPS[index].boss_id else ""
            row.configure(
                text=(
                    f"{index + 1:02d}. {ACT_ONE_MAPS[index].name}"
                    f"{boss_marker}  {status_text[status]}"
                ),
                fg_color=background,
                text_color=text_color,
            )

        definition = ACT_ONE_MAPS[campaign.map_index]
        self.current_map_title.configure(text=definition.name.upper())
        encounter_type = "Chefe do ato" if definition.boss_id else "Mapa comum"
        state_text = (
            "CONCLUÍDO"
            if campaign.act_completed
            else f"{campaign.victories}/{campaign.target}"
        )
        self.current_map_detail.configure(
            text=(
                f"MAPA       {campaign.map_number}/10\n"
                f"TIPO       {encounter_type}\n"
                f"PROGRESSO  {state_text}\n"
                f"RESUMO     {current_map_summary(campaign)}"
            )
        )
        self.next_objective_label.configure(text=next_objective(campaign))
