import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def extrair_palavras(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    secoes = soup.find_all("section")
    texto = " ".join(secao.get_text(separator=" ") for secao in secoes)

    palavras = re.findall(r'\b\w+\b', texto.lower())
    
    contagem = Counter(palavras)

    return contagem