try:
    import tkinter,tkinter.messagebox
    from tkinter import *
except:
    print('Instale o tkinter primeiro.')
try:
    from pytube import YouTube
except:
    print('instale o modulo pytube.')
import os,re


janela = tkinter.Tk()
janela.title("Youtube download")
janela.geometry("500x30")

e1=tkinter.StringVar()
e1.set("")

def paste(e1):
    e1.widget.event_generate('<Control-v>')

def download():
    url=e1.get()
    #bar = Progressbar(window, length=200)
    file = YouTube(url).streams.first()
    file.download(output_path="downloads")
    output_path = os.path.join("downloads", os.path.splitext(file)[0] + '.mp3')
    if os.path.exists(output_path):
        tkinter.messagebox.showinfo("Concluido","Concluido")
        print("Concluido")
    else:
        tkinter.messagebox.showerror("Erro","Aconteceu um erro\nE o video não pode ser baixado.")
    #bar['value'] = 70

def downloadmp3():
    url=e1.get()
    file = YouTube(url)
    final = file.streams.filter(only_audio=True)
    final[0].download(output_path="downloads")
    tgt_folder = "downloads"
    for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    	full_path = os.path.join(tgt_folder, file)
    	output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    	os.rename(full_path,output_path)
    os.system('cd ./downloads && rm -rf *.mp4')
    if os.path.exists(output_path):
        tkinter.messagebox.showinfo("Concluido","Concluido")
        print("Concluido")
    else:
        tkinter.messagebox.showerror("Erro","Aconteceu um erro\nE o video não pode ser baixado.")

l1 = Label(janela,text="Digite a URL").pack(side=LEFT)

exit = Button(janela,text = "Sair",command = janela.destroy).pack(side=RIGHT)
b1 = Button(janela,text = "Download MP4!",command = download).pack(side=RIGHT)
b2 = Button(janela,text = "Download MP3!",command = downloadmp3).pack(side=RIGHT)

e1=tkinter.Entry(janela)
e1.focus()
e1.pack()
e1.bind('<Return>',download)
e1.bind('<Button-3>',paste)


janela.mainloop()
