from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog, Button, Label, LEFT, RIGHT, N
from tkinter import ttk
import os.path
import config
import os

flag = 0
def runapp():
    class membuatStatus(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.window = parent
            self.initUI()
    
        def initUI(self):
            self.window.title("What's on your mind?")
            self.pack(fill=BOTH, expand=True)
    
            self.status()
            self.kirim()
            self.tombol()
        
        def tombol(self):
            tombolTutup = Button(self, text="Kirim", command=self.kirim)
            tombolTutup.pack(side=RIGHT, padx=5, pady=5)
    
            tombolOke = Button(self, text="Cancel", command=self.quit)
            tombolOke.pack(side=RIGHT)
    
        def kirim(self):
            try:
                global flag
                broadcast = self.masukkanKeWindow.get("1.0", "end")
                file_count = os.listdir("status")
                count = 1 + len(file_count)
                nama = "status/"+str(count)+".txt"
                print(count)
                if(flag == 0):
                    flag = 1
                else:
                    flag = 0
                    f = open(nama, "w")
                    f.write(broadcast)
                    f.close()
                    root.destroy()
                ttk.Label(mainframe, text="Status anda terkirim!").grid(row=9,sticky=N, columnspan=5)
            except:
                print("1")
    
        def status(self):
            teksField = Frame(self)
            teksField.pack(fill=BOTH, expand=True)
    
            self.teks = Label(teksField, text="Status :", width=6)
            self.teks.pack(side=LEFT, anchor=N, padx=5, pady=5)
    
            self.masukkanKeWindow = Text(teksField)
            self.masukkanKeWindow.pack(fill=BOTH, pady=5, padx=5, expand=True)
        
    root = Tk()
    root.geometry("300x450")
    app = membuatStatus(root)
    root.mainloop()