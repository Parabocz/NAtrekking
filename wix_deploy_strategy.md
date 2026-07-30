# Estratégia de Injeção de HTML do Wix e Bypass do Vite

## O Problema
Ao extrair arquivos HTML brutos do construtor antigo (Wix) e injetá-los no novo site (Vite/React/HTML estático), o Vite encontrava diversos erros de sintaxe no CSS original do Wix durante o processo de *build* no Vercel (ex: `Unknown word -bgh`, `Unknown word )`). O parser rigoroso do PostCSS do Vite interrompia o deploy imediatamente ao tentar ler as tags `<style>` aninhadas.

## A Solução (Implementada em generate_unified.py)
Para garantir que o código sujo do Wix nunca quebre o Vercel, a seguinte estratégia foi estabelecida:

1. **Separação de CSS e HTML:**
   O script Python (`generate_unified.py`) agora usa o BeautifulSoup para localizar e extrair todas as tags `<style>` do cabeçalho (`<head>`) do arquivo HTML fornecido.

2. **Isolamento Público (Bypass do Vite):**
   O conteúdo dessas tags `<style>` é aglomerado e salvo em um arquivo `.css` independente dentro da pasta `/public/wix/` (ex: `public/wix/wix_trekking-rinoceronte.css`). Arquivos na pasta `public` não são processados, compilados ou validados pelo *bundler* do Vite; eles são servidos como assets estáticos brutos.

3. **Injeção de Referência:**
   Em vez de injetar o CSS problemático diretamente na página gerada (`.html`), o gerador injeta apenas uma tag de link (`<link rel="stylesheet" href="/wix/wix_trekking-rinoceronte.css">`) imediatamente acima do conteúdo HTML bruto do Wix (a `div` `#SITE_PAGES`).

## Resumo da Regra para o Futuro
**Nunca injetar `<style>` brutos de plataformas terceiras no meio do HTML que passará por bundlers (Vite/Webpack). Sempre extrair o CSS para a pasta `/public` e linká-lo de forma externa.**
