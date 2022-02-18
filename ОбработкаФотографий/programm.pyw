import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image
from tkinter import messagebox
import sys

directory = None

class wtrmk(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_dir = tk.Button(self, text="Выбрите папку для сохранения\nготовой(ых) картинки(ок)",
                             command=self.choose_directory)
        btn_dir.pack(padx=60, pady=10)
        self.title('Обработчик фотографий by fReggy')
        w = self.winfo_screenwidth()//2-200
        h = self.winfo_screenheight()//2-125
        self.geometry('400x250+{}+{}'.format(w, h))
        self.minsize(400, 250)
        self.protocol("WM_DELETE_WINDOW", self.delt)

    def delt(self):
        self.destroy()
        sys.exit()
        

    def choose_directory(self):
        global directory
        directory = fd.askdirectory(title="Открыть папку для сохранения", initialdir="/")
        self.destroy()
        if len(directory) == 0:
            sys.exit()
            
        
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_watermark = tk.Button(self, text="Выберите watermark",
                             command=self.choose_water)
        btn_images = tk.Button(self, text="Выберите картинки",
                             command=self.choose_images)
        btn_watermark.pack(padx=60, pady=10)
        btn_images.pack(padx=60, pady=10)
        self.title('Обработчик фотографий by fReggy')
        w = self.winfo_screenwidth()//2-200
        h = self.winfo_screenheight()//2-125
        self.geometry('400x250+{}+{}'.format(w, h))
        self.minsize(400, 250)

    def choose_water(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть watermark", initialdir="/",
                                      filetypes=filetypes)
        global watermark
        if filename:
            watermark = Image.open(filename)
            watermark = watermark.resize((280, 109))
            
    def choose_images(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        flnm=fd.askopenfilenames(title="Открыть картинки", initialdir="/",
                                      filetypes=filetypes)
        kolvo = len(flnm)
        if kolvo:
            for i in range(kolvo):
                fullkartorig = Image.open(flnm[i])
                fullkart=fullkartorig
                fullkart =fullkart.convert('RGB')
                position = (fullkart.width - 300, fullkart.height - 130)
                fullkart.paste(watermark, position, watermark)
                b = str(i+1)
                konec = str(directory) + '/' + b + '.png'
                fullkart.save(konec)
                fullkartorig.close()
        if flnm:
            messagebox.showinfo('Обработчик фотографий by fReggy', 'Успешно обработано')
        

if __name__ == "__main__":
    wtrmk = wtrmk()
    while not directory:
        wtrmk.mainloop()
    app = App()
    app.mainloop()
