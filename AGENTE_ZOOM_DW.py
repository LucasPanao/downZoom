import json
from pprint import pprint
import requests
import os
import sys  
import urllib.request
import urllib3
import csv
import collections
import webbrowser
import time
from pathlib import Path
import shutil

# Função para retornar quando os downloads acabaram por usuário
def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 2000:
        print("Fazendo download...")
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    print("download terminado.")
    return seconds

#Abre a lista de e-mails e ids e faz a varredura delas, substituindo o id dentro da URL
files2 = open('list_emails.txt','r') 
files = open('list_ids.txt','r') #nessa lista ficará os IDs dos usuarios que serão baixados os arquivos
for line,line2 in zip(files.readlines(),files2.readlines()):
    id = line.strip('\n') 
    id2 = line2.strip('\n')
    url = "https://api.zoom.us/v2/users/%s/recordings?page_size=1000"%id 
    print (url)
    response = requests.get(url, headers={'Authorization': 'Bearer INSIRA SEU TOKEN AQUI '}) # Realiza o GET 
    data = response.json() 
    for meetings in data['meetings']:
        DownUrl = (meetings['recording_files'][0]['download_url'])
        webbrowser.open_new_tab(DownUrl)
        download_wait(r"C:\CAMINHO DA PASTA DE DOWNLOAD DO CHROME")       
    print("Todos os downloads terminaram, próximo usuário...")

    Path(r"SUA PASTA DE DESTINO\%s"%id2).mkdir(parents=True, exist_ok=True)
    source = r"C:\CAMINHO DA PASTA DE DOWNLOAD DO CHROME"
    destination = r"SUA PASTA DE DESTINO\%s"%id2

    #Verifica os arquivos baixadas pelo zoom e os coloca na pasta do usuario.
    for f in os.listdir(source):
        if f.endswith(".mp4") or f.endswith(".txt") or f.endswith(".m4a") :
            shutil.move(source+'\\'+f, destination)
    with open('%s.json'%id2, 'w') as f:json.dump(data, f) 
f.close() 
