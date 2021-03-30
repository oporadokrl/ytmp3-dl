########################
out_mp3='/sdcard/mp3'
out_mp4='/sdcard/mp4'
########################

import os,re

try:
	from pytube import YouTube
except:
	print('Deseja instalar as dependencias? [s/n]')
	choice = input('===>')
	if choice == 's' or choice == 'S':
		os.system('pip3 install pytube')
	else:
		exit()
	from pytube import YouTube	

CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'

arch = os.system('uname -a | grep -o "arm"')

if arch == "arm":
	f = open('path','r+')
	if os.path.exists('path'):
		pathing = f.read()
	else:
		pathing = input('Escreva o diretório do armazenamento: ')
		f.write(pathing)
	f.close
	out_mp3= '{}/mp3'.format(pathing)
	out_mp4= '{}/mp4'.format(pathing)

if os.path.exists('downloads'):
	pass
else:
	os.system('mkdir downloads')

Sair=False

while(Sair == False):
    os.system('clear')
    os.system('figlet -f slant "YATO"')
    print(f'{C}[{G}i{C}] Selecione o modo de operação')
    print(f'{C}[{G}1{C}] MP4')
    print(f'{C}[{G}2{C}] MP3')
    print()
    print(f'{C}[{G}0{C}] Sair')
    filetype = input('===>')
    
    if filetype == '0' or filetype == '00':
    	exit()
    
    print(f'{C}[{G}i{C}] Informe a url do video')
    url = input('===>')
    os.system('clear')
    os.system('figlet -f slant "YATO"')
    print(f'{C}[{G}i{C}] Baixando...por favor aguarde')
    
    if filetype == '1':
        file = YouTube(url).streams.first()
        file.download(output_path="downloads")
    
    if filetype == '2':
    	file = YouTube(url)
    	final = file.streams.filter(only_audio=True)
    	final[0].download(output_path="downloads")
    	tgt_folder = "downloads"
    	for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    		full_path = os.path.join(tgt_folder, file)
    		output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    		os.rename(full_path,output_path)
    	os.system('cd ./downloads && rm -rf *.mp4')
    
    print(f'{C}[{G}i{C}] Video baixado.')
    
    if arch == 'arm':
    	os.system('cd downloads && mv *.mp3 {} && mv *.mp4 {}'.format(out_mp3,out_mp4))
    
    print()
    print(f'{C}[{G}i{C}] Deseja baixar outro video?')
    print(f'{C}[{G}1{C}] Sim')
    print(f'{C}[{G}2{C}] Não')
    choice = input('===>')
    
    if choice != '1':
        Sair = True
