try:
    import tkinter,tkinter.messagebox
    from tkinter import *
    from tkinter.ttk import *
except:
    print('Instale o tkinter primeiro.')
    exit()
try:
    from pytube import YouTube
except:
    print('instale o modulo pytube.')
    exit()
import os,re


janela = tkinter.Tk()
janela.title("Youtube download")
janela.geometry("400x90")

e1=tkinter.StringVar()
e1.set("")

style = Style()
style.configure('W.TButton',foreground='black')
#style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'),foreground = 'red',background='black')

img1=PhotoImage(file='icon.png')
janela.iconphoto(False,img1)
janela.resizable(False, False)

if os.path.exists('listamp3'):
    os.remove('listamp3')
if os.path.exists('listamp4'):
    os.remove('listamp4')

def paste(e1):
    e1.widget.event_generate('<Control-v>')

def download():
    try:
        progress['value'] = 20
        janela.update_idletasks()
        url=e1.get()
        progress['value'] = 40
        janela.update_idletasks()
        file = YouTube(url).streams.first()
        progress['value'] = 60
        janela.update_idletasks()
        file.download(output_path="downloads")
        progress['value'] = 80
        janela.update_idletasks()
        progress['value'] = 90
        janela.update_idletasks()
        progress['value'] = 100
        janela.update_idletasks()
        tkinter.messagebox.showinfo("Concluido","Concluido")
        print("Concluido")
    except:
        tkinter.messagebox.showerror("Erro","Aconteceu um erro\nE o video não pode ser baixado.")
    e1.delete(0,'end')

def downloadmp3():
    progress['value'] = 0
    janela.update_idletasks()
    url=e1.get()
    progress['value'] = 20
    janela.update_idletasks()
    file = YouTube(url)
    progress['value'] = 40
    janela.update_idletasks()
    final = file.streams.filter(only_audio=True)
    progress['value'] = 50
    janela.update_idletasks()
    final[0].download(output_path="downloads")
    progress['value'] = 60
    janela.update_idletasks()
    tgt_folder = "downloads"
    for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    	full_path = os.path.join(tgt_folder, file)
    	output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    	os.rename(full_path,output_path)
    progress['value'] = 80
    janela.update_idletasks()
    os.system('cd ./downloads && rm -rf *.mp4')
    progress['value'] = 90
    janela.update_idletasks()
    if os.path.exists(output_path):
        progress['value'] = 100
        janela.update_idletasks()
        tkinter.messagebox.showinfo("Concluido","Concluido")
        print("Concluido")
    else:
        tkinter.messagebox.showerror("Erro","Aconteceu um erro\nE o video não pode ser baixado.")
    e1.delete(0,'end')

def adicionarlista():
    lista=open('listamp4','a')
    temp = str(e1.get() + ',')
    lista.write(temp)
    lista.close()

def adicionarlistamp3():
    lista=open('listamp3','a')
    temp = str(e1.get() + ',')
    lista.write(temp)
    lista.close()

def downloadlista():
    l1error=0
    lerror=0
    try:
        lista1=open('listamp3','r')
    except:
        l1error=1
        pass
    try:
        lista2=open('listamp4','r')
    except:
        lerror=1
        pass
    if lerror==1 and l1error==1:
        tkinter.messagebox.showerror("Erro","Nenhum item na lista.")
    elif lerror==0 and l1error==1:
        print('inicio')
    elif lerror==1 and l1error==0:
        print('inicio')
    elif lerror==0 and l1error==0:
        print('inicio')

progress = Progressbar(janela, orient = HORIZONTAL,length = 100, mode = 'determinate')
#progress.pack(side=BOTTOM)
progress.grid(row=1,column=3)

l1 = Label(janela,text="Digite a URL")
#l1.pack(side=LEFT)
l1.grid(row=1,column=1)

exit = Button(janela,style='W.TButton',text="Sair",command = janela.destroy)
#exit.pack(side=RIGHT)
exit.grid(row=3,column=2)

b1 = Button(janela,text = "Baixar MP4!",style='W.TButton',command = download)
#b1.pack(side=RIGHT)
b1.grid(row=2,column=3)

b2 = Button(janela,text = "Baixar MP3!",style='W.TButton',command = downloadmp3)
#b2.pack(side=RIGHT)
b2.grid(row=2,column=1)

b3 = Button(janela,text = "Adicionar a lista MP3",style='W.TButton',command = adicionarlistamp3)
b3.grid(row=3,column=1)

b4 = Button(janela,text = "Adicionar a lista MP4",style='W.TButton',command = adicionarlista)
b4.grid(row=3,column=3)

b5 = Button(janela,text = "Baixar lista",style="W.TButton",command = downloadlista)
b5.grid(row=2,column=2)

e1=tkinter.Entry(janela)
e1.focus()
#e1.pack(side=LEFT)
e1.grid(row=1,column=2)
e1.bind('<Return>',download)
e1.bind('<Button-3>',paste)

janela.mainloop()
