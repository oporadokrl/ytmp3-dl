import pytube,moviepy,os
from pytube import YouTube
import moviepy.editor as mp
import re

CO='\033[m'
R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'

########################
termux='1'
out_mp3='/sdcard/mp3'
out_mp4='/sdcard/mp4'
########################

Sair=False

while(Sair == False):
    os.system('figlet -f slant "YATO"')
    print(f'{C}[{G}i{C}] Selecione o modo de operação')
    print(f'{C}[{G}1{C}] MP4')
    print(f'{C}[{G}2{C}] MP3')
    print()
    print(f'{C}[{G}3{C}] Sair')
    filetype = input('===>')
    if filetype == '3' or filetype == '03':
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
    	final = file.streams.filter(only_audio=True).all()
    	final[0].download(output_path="downloads")
    	tgt_folder = "downloads"
    	for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    		full_path = os.path.join(tgt_folder, file)
    		output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    		clip = mp.AudioFileClip(full_path).subclip(10,)
    		clip.write_audiofile(output_path)
    	os.system('cd ./downloads && rm -rf *.mp4')
    print(f'{C}[{G}i{C}] Video baixado.')
    if termux == '1':
    	os.system('cd downloads && mv *.mp3 {} && mv *.mp4 {}'.format(out_mp3,out_mp4))
    print()
    print(f'{C}[{G}i{C}] Deseja baixar outro video?')
    print(f'{C}[{G}1{C}] Sim')
    print(f'{C}[{G}2{C}] Não')
    choice = input('===>')
    if choice != '1':
        Sair = True
