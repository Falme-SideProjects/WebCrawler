__author__ = 'USER'

import webbrowser
import requests
from bs4 import BeautifulSoup

ListArtist = ["Fear,and Loathing in Las Vegas"]

#NomeArtista = raw_input("Nome : ");
#webbrowser.open('http://thepiratebay.se/search/'+Resultado+'/0/7/100');


def SearchSong(Lista):
    for Resultado in Lista:
        Recebido = 0
        url = 'http://thepiratebay.se/search/'+(str(Resultado))+'/0/7/100'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            if Recebido == 0:
                LinkRecebido = link.get("href")
                if LinkRecebido[:6] == "magnet":
                    webbrowser.open(LinkRecebido)
#                   print(LinkRecebido)
                    Recebido = 1


SearchSong(ListArtist)
#SearchSong(NomeArtista)
