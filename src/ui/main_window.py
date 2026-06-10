from collections import deque
from pathlib import Path

import customtkinter as ctk

from combat.combat import CombatEngine
from hero.hero import Hero
from save.save_manager import SaveManager


class MainWindow(ctk.CTk):
    COMBAT_INTERVAL_MS = 800
    SAVE_INTERVAL_MS = 10_000

    def __init__(self, hero: Hero, save_manager: SaveManager) -> None:
        super().__init__()
        self.hero = hero
        self.save_manager = save_manager
        self.combat = CombatEngine(hero)
        self.log_lines: deque[str] = deque(maxlen=10)

        self.title("TBH2")
        self.geometry("300x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self._build_ui()
        self._append_log(
            f"Um {self.combat.enemy.name} nível {self.combat.enemy.level} apareceu."
        )
        self._refresh()
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _build_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)

        self.hero_label = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=18, weight="bold")
        )
        self.hero_label.grid(row=0, column=0, padx=14, pady=(12, 2), sticky="w")

        self.stats_label = ctk.CTkLabel(self, text="", anchor="w")
        self.stats_label.grid(row=1, column=0, padx=14, sticky="ew")

        self.hp_label = ctk.CTkLabel(self, text="", anchor="w")
        self.hp_label.grid(row=2, column=0, padx=14, pady=(8, 0), sticky="ew")
        self.hp_bar = ctk.CTkProgressBar(self, progress_color="#b83b3b")
        self.hp_bar.grid(row=3, column=0, padx=14, sticky="ew")

        self.xp_label = ctk.CTkLabel(self, text="", anchor="w")
        self.xp_label.grid(row=4, column=0, padx=14, pady=(7, 0), sticky="ew")
        self.xp_bar = ctk.CTkProgressBar(self, progress_color="#3b78b8")
        self.xp_bar.grid(row=5, column=0, padx=14, sticky="ew")

        self.enemy_label = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=15, weight="bold")
        )
        self.enemy_label.grid(row=6, column=0, padx=14, pady=(14, 2), sticky="w")
        self.enemy_hp_bar = ctk.CTkProgressBar(self, progress_color="#8c4ab8")
        self.enemy_hp_bar.grid(row=7, column=0, padx=14, sticky="ew")

        equipment_title = ctk.CTkLabel(
            self, text="Equipamento", font=ctk.CTkFont(weight="bold")
        )
        equipment_title.grid(row=8, column=0, padx=14, pady=(14, 0), sticky="w")
        self.equipment_label = ctk.CTkLabel(
            self, text="", justify="left", anchor="w"
        )
        self.equipment_label.grid(row=9, column=0, padx=14, sticky="ew")

        log_title = ctk.CTkLabel(
            self, text="Combate", font=ctk.CTkFont(weight="bold")
        )
        log_title.grid(row=10, column=0, padx=14, pady=(12, 0), sticky="w")
        self.log_box = ctk.CTkTextbox(self, height=150, state="disabled", wrap="word")
        self.log_box.grid(row=11, column=0, padx=14, pady=(2, 12), sticky="nsew")
        self.grid_rowconfigure(11, weight=1)

    def _combat_tick(self) -> None:
        important_event = False
        for event in self.combat.tick():
            self._append_log(event.message)
            if event.kind in {"victory", "defeat", "level_up", "loot"}:
                important_event = True
        if important_event:
            self.save_manager.save(self.hero)
        self._refresh()
        self.after(self.COMBAT_INTERVAL_MS, self._combat_tick)

    def _autosave(self) -> None:
        self.save_manager.save(self.hero)
        self.after(self.SAVE_INTERVAL_MS, self._autosave)

    def _refresh(self) -> None:
        enemy = self.combat.enemy
        self.hero_label.configure(text=f"{self.hero.name}  •  Nível {self.hero.level}")
        self.stats_label.configure(
            text=f"ATK {self.hero.attack}    DEF {self.hero.defense}"
            f"    Vitórias {self.hero.enemies_defeated}"
        )
        self.hp_label.configure(
            text=f"HP  {self.hero.current_hp} / {self.hero.max_hp}"
        )
        self.hp_bar.set(self.hero.current_hp / self.hero.max_hp)
        self.xp_label.configure(text=f"XP  {self.hero.xp} / {self.hero.xp_needed}")
        self.xp_bar.set(self.hero.xp / self.hero.xp_needed)
        self.enemy_label.configure(
            text=(
                f"{enemy.name} Nv. {enemy.level}"
                f"  •  HP {enemy.current_hp}/{enemy.max_hp}"
            )
        )
        self.enemy_hp_bar.set(enemy.current_hp / enemy.max_hp)

        weapon = self.hero.equipment["weapon"]
        armor = self.hero.equipment["armor"]
        weapon_text = (
            f"{weapon.name} (+{weapon.attack_bonus} ATK)" if weapon else "Nenhuma"
        )
        armor_text = (
            f"{armor.name} (+{armor.defense_bonus} DEF)" if armor else "Nenhuma"
        )
        self.equipment_label.configure(
            text=f"Arma: {weapon_text}\nArmadura: {armor_text}"
        )

    def _append_log(self, message: str) -> None:
        self.log_lines.append(message)
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.insert("end", "\n".join(self.log_lines))
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def _on_close(self) -> None:
        self.save_manager.save(self.hero)
        self.destroy()


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]

