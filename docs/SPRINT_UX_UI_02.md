# Sprint UX/UI 02 - Interface Taskbar Expandida

## Objetivo

Separar a jornada contínua do gerenciamento detalhado por meio de dois modos de
interface:

- modo compacto para acompanhamento passivo;
- modo expandido para decisões de personagem, itens e mundo.

## Status

In Progress

## Dependências

- [UI e UX](core/05_UI_UX.md)
- [Identidade de Taskbar](taskbar/01_TASKBAR_IDENTITY.md)
- [Sistema de herói](heroes/01_HERO_SYSTEM.md)
- [Sistema de itens](items/01_ITEM_SYSTEM.md)
- [Estrutura do mundo](maps/01_WORLD_STRUCTURE.md)
- [Arquitetura técnica](technical/05_ARCHITECTURE.md)

## Visão Geral

O modo compacto permanece em `360x600` e mantém a jornada visível. Os botões
Herói, Mochila e Mapa abrem uma janela de gerenciamento em `800x600`. Abrir,
alternar ou fechar painéis não pausa o loop do jogo.

O wireframe de referência foi fornecido como:

- `Sprint UX-UI 02 - Interface Taskbar Expandida.pdf`;
- `ChatGPT Image 11 de jun. de 2026, 11_32_31.png`.

## Estrutura

### Modo Compacto

- cabeçalho com nível e ouro;
- ato, mapa e progresso;
- jornada visual;
- última ação relevante;
- resumo do herói;
- navegação para os painéis expandidos.

### Painel Herói

- sprite ampliado;
- atributos atuais;
- Power e Build Score;
- dez slots oficiais;
- estados `Vazio` e `Indisponível` para sistemas futuros.

### Painel Mochila

- filtros por categoria;
- grid paginado de vinte itens;
- raridade e Power;
- comparação com item equipado;
- equipamento manual;
- ações futuras apresentadas como desabilitadas.

### Painel Mapa

- dificuldade e ato;
- dez mapas;
- estados concluído, atual e bloqueado;
- marco de chefe;
- próximo objetivo;
- comunicação pós-chefe.

## Regras

- O modo expandido não substitui a jornada compacta.
- O loop continua executando com o painel aberto.
- A interface não cria regras novas de combate, loot ou progressão.
- Recursos ainda ausentes devem aparecer desabilitados ou como preparação.
- O idioma principal da interface é português.
- Ações detalhadas devem permanecer fora da janela compacta.

## Dados

Arquivos principais:

- `src/ui/main_window.py`;
- `src/ui/expanded_window.py`;
- `src/ui/presentation.py`;
- `src/ui/journey_scene.py`.

Validação:

- suíte automatizada com 26 testes;
- importação e compilação verificadas;
- inspeção visual dos três painéis;
- save temporário usado durante capturas.

## Pendências

- Criar ícones próprios para slots e categorias.
- Implementar favoritos, bloqueio e venda no domínio.
- Implementar troca de mapa e Free Farm.
- Integrar classe, atributos avançados e habilidades.
- Avaliar responsividade além de `800x600`.
- Refinar tema visual para aproximar a arte final do wireframe.

## Histórico de Alterações

- 2026-06-11: implementados os modos compacto e expandido.
- 2026-06-11: adicionados painéis Herói, Mochila e Mapa.
- 2026-06-11: adicionada paginação do inventário e comunicação pós-chefe.
