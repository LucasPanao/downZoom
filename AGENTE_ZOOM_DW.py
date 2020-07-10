import json
import requests
import os
import webbrowser
import time
from pathlib import Path
import shutil
from os.path import basename
from urllib.request import urlopen
import configparser



# Função para retornar quando os downloads acabaram por usuário
def download_wait(path_):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 2000:
        print("Fazendo download...")
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    print("download terminado.")
    return seconds

#Configurando arquivo .ini que contém os caminhos das pastas
configParser = configparser.RawConfigParser()   
configFilePath = "path.ini"
configParser.read(configFilePath)

### DECLARAÇÕES 
path_ = configParser.get('my-path', 'path1')
path_v = configParser.get('my-path', 'path1_v')
####

#Abre a lista de e-mails e ids e faz a varredura delas, substituindo o id dentro da URL
files2 = open('list_emails.txt','r') 
files = open('list_ids.txt','r') #nessa lista ficará os IDs dos usuarios que serão baixados os arquivos
for line,line2 in zip(files.readlines(),files2.readlines()):
    log = open(path_ + r'\log.txt','w')  # Arquivo de LOG
    id = line.strip('\n') 
    id2 = line2.strip('\n')
    url = "https://api.zoom.us/v2/users/%s/recordings?page_size=1000"%id 
    hdr = 'INSIRA SEU TOKEN AQUI'
    url = (url + hdr)
    response = requests.get(url) # Realiza o GET 
    data = response.json() 
    for meetings in data['meetings']:
        ReuniaoId = (meetings['id'])
        rec_files = (meetings['recording_files'])
        for k in rec_files:
            DownUrl = (k['download_url'])
            GravacaoId = (k['id'])
            url = DownUrl + hdr
            response = urlopen(url)
            arq_name = basename(response.url)
            arq, tsh = arq_name.split("?", 1)
            log.write(str(ReuniaoId) + ";" + GravacaoId + ";" + arq + "\n") #Escreve os ids e nome do arq dentro do log
            webbrowser.open_new_tab(url)
        download_wait(path_)       
    print("Todos os downloads terminaram, próximo usuário...")
    log.close()
    Path(path_v%id2).mkdir(parents=True, exist_ok=True)
    source = path_
    destination = path_v%id2

    #Verifica os arquivos baixadas pelo zoom e os coloca na pasta do usuario.
    for f in os.listdir(source):
        if f.endswith(".mp4") or f.endswith(".txt") or f.endswith(".m4a") :
            shutil.move(source+'\\'+f, destination)
    with open('%s.json'%id2, 'w') as f:json.dump(data, f) 
f.close() 
