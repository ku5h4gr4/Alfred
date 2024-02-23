from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from time import sleep
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1300x700")

def scrBg():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("Z:/Stuffs/Project/AI/Images/AI_bg.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    mixer.music.load("Z:/Stuffs/Project/AI/Sounds/ai_bg_sound_044858.mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1300, 700))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        sleep(0.05)
    root.destroy()


scrBg()
root.mainloop()
