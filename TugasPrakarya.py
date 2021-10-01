# Prakarya
# Di-Buat (Arya Danendra/8 Purnawarman/6)

import threading
import tkinter
import winsound
from tkinter import *
from winsound import *
from PIL import Image, ImageTk

root = Tk()
root.title("Tugas Prakarya")
root.iconbitmap("C:/Users/Asrock/Downloads/kisspng-junior-high-school-stella-duce-1-tarakanita-1-seni-sma-stella-duce-2-5b619ac1016d43.5402541315331232650059.ico")
root.geometry("1000x600")

image1 = Image.open(r"C:/Users/Asrock/Downloads/kissclipart-cow-transparent-background-clipart-holstein-friesi-aabf16afe16c0010.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

label1.place(x=0, y=0)

def playsound():
    winsound.PlaySound("C:/Users/Asrock/Downloads/mixkit-cow-single-moo-1747.wav", winsound.SND_ALIAS)


def play():
    threadsound = threading.Thread(target=playsound)
    threadsound.start()

button = Button(root, text = 'Bunyikan Suara', font=("helvetica", 24), command = play)
button.pack()

root.mainloop()



