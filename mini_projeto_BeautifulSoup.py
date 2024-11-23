from bs4 import BeautifulSoup
import requests
import re

#bloco para conectar ao site
link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")

tbody = site.find('tbody') # localiza a tabela no site. A tabela está em um tbody
linhas = tbody.find_all('tr') # dentro da tabela do site, localize todas as linhas. Linhas dentro de tr.
moedas = {} # vai receber o nome da moeda e o dict dela

# for para percorrer as linhas da tabela e buscar as informações nelas
for linha in linhas:
    try:
        nome = linha.find(class_="iPbTJf").text #pega o nome da moeda
        codigo = linha.find(class_="coin-item-symbol").text # pega a sigla dela
        valores = linha.find_all(string=re.compile(r"\$")) # pega todos os valores que contém $ na linha
        preco = valores[0] # o preço é o meu primeiro índice na linha, por isso ele acessou valores e pegou o zero.
        percentuais = linha.find_all(string=re.compile("%")) # pega todos os valores que contém % na linha
        
        """ O objetivo deste for é para caso ele encontre valor negativo, deverá colocar o '-' antes do percentual.
        por padrão, não estava vindo negativo. exemplo: -36% estava vindo 36%"""
        for i, percentual in enumerate(percentuais):
            if "bQjSqS" in percentual.parent["class"]:
                percentuais[i] = "-" + str(percentual)
                
        # cada var recebe o seu valor de acordo com a posição no site       
        var_1h = percentuais[0]
        var_24h = percentuais[1]
        var_7d = percentuais[2]
        
        market_cap = valores[2]
        volume = valores[3]
        
        # dicionário para receber as informações de cada moeda
        dic = {'Nome': nome, 'Código': codigo,'Preço': preco, 'Market Cap': market_cap, 'Volume': volume, '1h %': var_1h, '24h %': var_24h, '7d %': var_7d}
        moedas[nome] = dic

    except AttributeError: # serve apenas para ignorar o erro de AttributeError
        break

# for para deixar a saída arrumada  
for nome, dados in moedas.items():
    print(f'{nome}:')
    for chave, valor in dados.items():
        print(f"    {chave}: {valor}")
    print('-' * 30)
    