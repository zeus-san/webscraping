import requests
from bs4 import BeautifulSoup
def substituir(string)

def pprint(algo):
    print(algo.prettify())
#https://www.amazon.com.br/s?k={key} 
def consulta_amazon(key):
    res = requests.get(f"https://www.amazon.com.br/s?k={key}")
    soup = BeautifulSoup(res.content,'html.parser')
    produtos = soup.find_all('div',class_="a-section a-spacing-base")
    for produto in produtos[:10]:
        nome = produto.find('span',class_='a-size-base-plus a-color-base a-text-normal').text
        valor = produto.find('span',class_='a-offscreen').text
        link = 'https://www.amazon.com.br' + produto.find('a',class_='a-link-normal s-no-outline')['href']
        img = produto.find('img',class_='s-image')['src']


#https://lista.mercadolivre.com.br/{key}#D[A:{key}]
def consulta_mercadolivre(key):
    res = requests.get(f"https://lista.mercadolivre.com.br/{key}#D[A:{key}]")
    soup = BeautifulSoup(res.content,'html.parser')
    divs = soup.find_all('li',class_="ui-search-layout__item shops__layout-item")
    for i in divs[:10]:
        nome = i.h2.text
        valor = i.find('span',class_='price-tag-fraction').text
        link = i.find('a')['href']
        img = i.img['data-src']


#https://www.magazineluiza.com.br/busca/{key}/

def consulta_magazineluiza(key):
    res = requests.get(f"https://www.magazineluiza.com.br/busca/{key}/")
    soup = BeautifulSoup(res.content,'html.parser')
    divs = divs=soup.find_all('li',class_="sc-fCBrnK hYPKVt")
    for i in divs[:10]:
        nome = i.h2.text
        valor = i.find('p',attrs={'data-testid':"price-value"}).text
        link = "https://www.magazineluiza.com.br" + i.a['href']
        img = i.img['src']


#https://www.americanas.com.br/busca/{key}
def consulta_americanas(key):
    headers = { 'Accept-Language' : 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.0.0'}
    res = requests.get(f"https://www.americanas.com.br/busca/{key}",headers=headers)
    soup = BeautifulSoup(res.content,'html.parser')
    divs = soup.find_all('div',class_="col__StyledCol-sc-1snw5v3-0 jGlQWu src__ColGridItem-sc-122lblh-1 cJnBan")
    for i in divs[:10]:
        nome = i.h3.text
        valor = i.find('span',class_='src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM').text
        link = "https://www.americanas.com.br" + i.a['href']
        img = i.img['src']






headers = { 'Accept-Language' : 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.0.0'}
















