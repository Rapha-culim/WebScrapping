## Scraping de Preços de Tibia Gold na DFG

Este script Python, `Tibia.py`, utiliza as bibliotecas `requests` e `beautifulsoup4` para realizar a raspagem (scraping) de dados de anúncios de venda de Tibia Gold no site DFG.

### Pré-requisitos

Para executar este script, você precisa ter o Python instalado e as seguintes bibliotecas Python:

  * `requests`
  * `beautifulsoup4`

Você pode instalá-las usando `pip`:

```bash
pip install requests beautifulsoup4
```

### O que o script faz

A função principal, `scrape_dfg_tibia_gold()`, realiza os seguintes passos:

1.  **Define a URL:** Aponta para a página de vendas de Tibia Gold da DFG (`https://www.dfg.com.br/pt-PT/tibia/gold/`).
2.  **Define um User-Agent:** Utiliza um `User-Agent` para simular uma requisição de navegador, o que é uma boa prática ao fazer scraping.
3.  **Faz a Requisição:** Envia uma requisição GET para a URL e verifica se a resposta foi bem-sucedida (`resp.raise_for_status()`).
4.  **Parsing com BeautifulSoup:** Analisa o conteúdo HTML da página.
5.  **Extrai os Dados:** Itera sobre os elementos `<h4>` no HTML e extrai informações relacionadas a cada anúncio de gold, como:
      * `title` (Título do anúncio)
      * `price` (Preço)
      * `sales` (Informações de vendas, geralmente em um parágrafo `<p>` próximo)
      * `vendor` (Nome do vendedor/loja, extraído de um link `<a>` próximo)
6.  **Retorna os Anúncios:** Retorna uma lista de dicionários, onde cada dicionário representa um anúncio.

### Como executar

Execute o script diretamente:

```bash
python Tibia.py
```

### Saída

Quando executado como script principal (`if __name__ == "__main__":`), ele chama a função e imprime no console a lista de anúncios de gold.

**Exemplo de Saída (formato de dicionário):**

```
{'title': 'Oferta Tibia 100kk Gold', 'price': 'R$ 20,00', 'sales': '350+ Vendas', 'vendor': 'VendedorXYZ'}
{'title': 'Tibia 50kk Gold Promocao', 'price': 'R$ 10,50', 'sales': '120 Vendas', 'vendor': 'LojaABC'}
# ... e assim por diante
```

**Nota:** A estrutura HTML da página alvo (`https://www.dfg.com.br/pt-PT/tibia/gold/`) é crucial para o funcionamento deste script. Se a DFG alterar o layout do site (classes, IDs ou a hierarquia dos elementos), o seletor CSS utilizado no script (`soup.select("h4")`, `h4 + *`, `p`, `a`) precisará ser ajustado.
