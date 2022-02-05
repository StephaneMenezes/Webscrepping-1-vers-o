from re import I
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

options = Options()

options.add_argument('window-size=1024,768')

navegador = webdriver.Chrome(options=options)
i = 1 
novosprodutos = []

for i in range(1,5):
    navegador.get('https://www.EXEMPLO DE SITE QUE NECESSITA INTERAÇÃO'+str(i))
    sleep(30)
    site = BeautifulSoup(navegador.page_source, 'html.parser')

    # Div com as informações sobre os produtos
    produto = site.findAll("div", attrs={'class': 'card-footer'})
    # print(produto)
  

    for produtos in produto:
    
        titulo = produtos.find("h4", attrs={'class': 'thumbnail-label'})

        link = produtos.find("a", attrs={'class': 'thumbnail-name'})

        ref = produtos.find("div", attrs={'class': 'x-product__id'})

        preco = produtos.find("span", attrs={'class': 'x-after loaded'})    

        link_completo = "https://www.leomadeiras.com.br"+link["href"]

        categoria = "Madeiras"
        #tipo_produto = titulo.text[0:10]
        # lista_produtos.append([titulo.text,preco.text, link['href'],ref.text,tipo_produto,metatag,titulo.text])
        novosprodutos.append([titulo.text, link_completo, categoria])
       
        #seo_leo=pd.DataFrame(novosprodutos, columns=["Título", "Preço","Link","Referência do produto","tipo do produto","Description","title"])  
seo_leo = pd.DataFrame(novosprodutos, columns=["Título", "Link", "Categoria"])
seo_leo.to_csv('seo_compensados.xlsx', index=False)
