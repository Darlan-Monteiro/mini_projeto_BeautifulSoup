# mini_projeto_BeautifulSoup

Web Scraper de Criptomoedas
Este é um projeto em Python que utiliza as bibliotecas BeautifulSoup, requests e re para realizar o web scraping do site CoinMarketCap. O script coleta informações sobre criptomoedas e organiza os dados em um formato legível.

Funcionalidades
Conexão com o site CoinMarketCap para buscar dados atualizados.
Extração de informações como:
Nome da criptomoeda
Código (sigla)
Preço
Market Cap
Volume
Variações de preço em 1h, 24h e 7 dias.
Ajuste para exibir valores negativos corretamente (ex.: -36%).
Impressão dos dados extraídos de forma organizada.


Pré-requisitos
Certifique-se de ter o Python instalado e as seguintes bibliotecas disponíveis no seu ambiente:

BeautifulSoup (disponível no pacote bs4)
requests
re (biblioteca padrão do Python)
Para instalar as dependências necessárias, você pode usar o comando:
    pip install beautifulsoup4 requests
