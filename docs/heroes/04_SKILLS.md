# Habilidades

## Objetivo

Definir habilidades automáticas e sua relação com classes, atributos e combate.

## Status

Planned - Fase 3

## Dependências

- [Classes](02_CLASSES.md)
- [Atributos](03_ATTRIBUTES.md)
- [Raças](05_RACES.md)
- [Combate](../core/03_COMBAT.md)

## Modelo de Ativação

O combate permanece automático por padrão. Habilidades devem operar por autocast
e condições legíveis, sem exigir barra de ação ou microgerenciamento.

Configurações planejadas:

- ativar ou desativar cada habilidade;
- ordenar prioridades;
- permitir cast manual opcional em uma fase posterior;
- manter ataque básico como fallback.

## Recargas e Condições

Cada habilidade pode considerar:

- recarga;
- recurso futuro;
- vida própria ou do alvo;
- quantidade de inimigos ou aliados;
- prioridade configurada.

INT poderá reduzir recarga e ampliar cura quando essas conversões forem
implementadas.

## Habilidades por Classe

Cada arquétipo precisa de uma rotação automática reconhecível:

- Tank: mitigação, proteção e controle;
- Healer: cura, sustentação e suporte;
- DPS: dano e execução.

Passivas raciais usam a mesma infraestrutura de efeitos, mas não precisam seguir
o autocast.

## Feedback Visual

- indicar habilidade ativada sem esconder o combate;
- diferenciar ataque básico, cura e defesa;
- evitar excesso de texto e efeitos na janela compacta;
- permitir leitura rápida de recarga ou disponibilidade.

## Regras

- Habilidades só entram após a validação de classes e atributos.
- Autocast é o comportamento principal.
- Desativar habilidades não pode travar o combate.
- Cast manual é opcional e não está aprovado para a primeira implementação.
- Prioridade deve usar identificadores persistentes e defaults válidos.

## Pendências

- Definir uma habilidade inicial por arquétipo.
- Definir modelo de prioridade.
- Definir representação compacta de recarga.

## Histórico de Alterações

- 2026-06-10: autocast e configuração alinhados ao briefing.
- 2026-06-10: criado o template modular.
