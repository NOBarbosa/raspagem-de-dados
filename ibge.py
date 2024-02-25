import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapin_uf(uf: str):
  uf_url = f"https://www.ibge.gov.br/cidades-e-estados/{uf}.html"
  page = requests.get(uf_url)

  soup = BeautifulSoup(page.content, 'html.parser')

  indicadores = soup.select('.indicador')

  uf_dict = {
    dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
    for dado in indicadores
  }

  return uf_dict
  # return indicadores[0].text


# for indicador in estado:


ufs = [
  'ac', 
  'al', 
  'ap', 
  'am', 
  'ba', 
  'ce', 
  'df', 
  'es',  
  'go', 
  'ma', 
  'mt',  
  'ms', 
  'mg', 
  'pa', 
  'pb', 
  'pr', 
  'pe', 
  'pi', 
  'rj', 
  'rn',  
  'rs',  
  'ro', 
  'rr', 
  'sc',  
  'sp',  
  'se', 
  'to'  
]
for uf in ufs:
  print(scrapin_uf(uf))