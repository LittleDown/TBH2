# Arquivo Histórico

## Objetivo

Preservar GDDs, briefings, relatórios, revisões e documentos anteriores à arquitetura modular do TBH2.

Este diretório existe para manter rastreabilidade histórica do projeto.

Os documentos arquivados podem ser consultados para entender decisões anteriores, mas não devem ser usados como fonte principal de implementação.

---

## Status

Approved

---

## Dependências

* [Índice atual](../README.md)
* [Roadmap](../technical/04_ROADMAP.md)
* [Arquitetura técnica](../technical/05_ARCHITECTURE.md)

---

# Visão Geral

Os arquivos deste diretório representam fases anteriores do projeto.

Eles podem conter:

* decisões antigas;
* nomenclaturas substituídas;
* sistemas legados;
* propostas descartadas;
* versões anteriores do GDD;
* briefings enviados ao Codex;
* relatórios de sprint;
* registros de demo técnica.

Após a migração para documentação modular, a fonte principal de verdade passou a ser o conjunto de documentos ativos organizados por domínio.

---

# Função do Arquivo Histórico

O histórico serve para:

* preservar contexto;
* explicar a evolução do projeto;
* evitar perda de decisões importantes;
* permitir auditoria de mudanças;
* registrar material usado em fases anteriores;
* apoiar migração de decisões ainda válidas.

O histórico não serve para orientar implementação direta quando houver documento modular atualizado.

---

# Estrutura

Este diretório pode conter:

* GDD inicial;
* revisões refinadas;
* visão e loop anteriores;
* relatórios técnicos;
* briefings de Codex;
* documentos de sprint;
* auditorias;
* versões antigas de roadmap;
* registros de decisões substituídas.

---

# Fonte de Verdade

Documentos arquivados não são fonte principal.

Regra:

```text
Documento ativo existe
↓
Usar documento ativo

Documento ativo não existe
↓
Consultar histórico como referência

Decisão histórica ainda é válida
↓
Migrar para o documento modular proprietário
```

Nenhuma decisão deve permanecer apenas no arquivo histórico se ainda for relevante para implementação futura.

---

# Regras

* Não usar documentos arquivados como fonte principal de implementação.
* Não remover histórico sem decisão registrada.
* Não editar documentos históricos para parecerem atuais.
* Não misturar documentação ativa com documentação arquivada.
* Não usar GDD antigo contra decisões aprovadas nos documentos modulares.
* Decisões válidas encontradas no histórico devem ser migradas para o domínio correto.
* Documentos históricos devem preservar contexto, data e origem sempre que possível.

---

# Exemplos de Uso Correto

Uso correto:

* consultar um briefing antigo para entender por que uma decisão foi tomada;
* comparar versões anteriores do GDD;
* recuperar uma ideia válida ainda não migrada;
* auditar mudanças feitas durante uma sprint;
* identificar sistemas legados.

Uso incorreto:

* implementar uma feature baseada apenas em GDD antigo;
* reativar sistema removido sem revisar documentação atual;
* usar briefing antigo como fonte superior ao Roadmap;
* copiar regras antigas para o código sem validação.

---

# Dados

* Diretório: `archive/`
* Finalidade: preservação histórica
* Fonte principal atual: documentação modular
* Status documental: Approved
* Idioma principal: português
* Formato: Markdown compatível com GitHub

---

# Pendências

* Revisar documentos antigos.
* Migrar decisões ainda válidas.
* Identificar documentos obsoletos.
* Registrar origem de cada arquivo histórico.
* Criar lista de versões arquivadas.
* Separar relatórios técnicos de GDDs antigos.
* Marcar sistemas legados que não devem retornar.

---

# Histórico de Alterações

* 2026-06-10: criado durante a migração modular.
* 2026-06-10: definida distinção entre documentação ativa e documentação histórica.
* 2026-06-10: adicionadas regras para consulta e migração de decisões antigas.
