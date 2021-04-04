try:
    from pytube import YouTube
except:
    print('Falha ao importar,\nverifique se você tem o módulo pytube instalado.')
    exit()
import os
def download(url,form="mp3",tgt_folder="downloads"):
    if form == "mp4":
        file = YouTube(url).streams.first()
        file.download(output_path="downloads")
    elif form == "mp3":
        file = YouTube(url)
        final = file.streams.filter(only_audio=True)
        final[0].download(output_path="downloads")
        tgt_folder = "downloads"
        for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
            full_path = os.path.join(tgt_folder, file)
            output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
            os.rename(full_path,output_path)
    return file
        #os.system('cd ./downloads && rm -rf *.mp4')
