# Assets do Arqueiro MVP

Esta pasta implementa o contrato visual da classe `archer`.

Os sprites foram gerados como uma folha consistente, tiveram o fundo cromatico
removido e foram recortados em frames transparentes de 512x512.

Arquivos usados em runtime:

- `idle.png`
- `walk1.png`
- `walk2.png`
- `combat_idle.png`
- `attack1.png`
- `attack2.png`
- `hit.png`
- `victory.png`
- `defeat.png`
- `front.png`

`source_sprite_sheet_alpha.png` preserva a folha de origem transparente para
ajustes futuros e nao e carregada pelo jogo.

## Prompt de geracao

```text
Create a 5-column by 2-row game sprite sheet of the same fantasy human archer
on a flat chroma-key background. Include idle, two walking poses, combat aim,
bow draw, bow release, hit, victory, defeat and front-facing stance. Agile
young archer with short brown hair, green leather armor, brown boots, dark red
cape, wooden recurve bow and quiver. Polished hand-painted 2D fantasy game
sprite, crisp silhouette, consistent scale and baseline, readable at 84px.
```

Geracao realizada com a ferramenta integrada de imagens do Codex em
2026-06-11. O projétil exibido durante o jogo e desenhado pela UI e nao faz
parte do calculo de dano.
