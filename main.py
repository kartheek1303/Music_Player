import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

screen = tk.Tk()
screen.title("CSK music player")
screen.geometry("800x800")
screen.config(bg= "black")

pattern = "*.mp3"
mixer.init()
prev_img = ImageTk.PhotoImage(Image.open('back.png'))
next_img = ImageTk.PhotoImage(Image.open('next.png'))
pause_img = ImageTk.PhotoImage(Image.open('pause.png'))
play_img = ImageTk.PhotoImage(Image.open('play.png'))
stop_img = ImageTk.PhotoImage(Image.open('stop.png'))

def select():
    currentsong.config(text=lb.get('anchor'))
    mixer.music.load(fn+'//'+lb.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    lb.select_clear('active')
    currentsong.config(text='')

def play_next():
    next_song = lb.curselection()
    next_song = next_song[0] + 1
    next_song_name = lb.get(next_song)
    currentsong.config(text = next_song_name)
    mixer.music.load(fn+'//'+next_song_name)
    mixer.music.play()

    lb.select_clear(0,'end')
    lb.activate(next_song)
    lb.select_set(next_song)

def play_prev():
    next_song = lb.curselection()
    next_song = next_song[0] - 1
    next_song_name = lb.get(next_song)
    currentsong.config(text = next_song_name)
    mixer.music.load(fn+'//'+next_song_name)
    mixer.music.play()

    lb.select_clear(0,'end')
    lb.activate(next_song)
    lb.select_set(next_song)


def searchFiles():
    global fn
    fn = filedialog.askdirectory()
    for root,dirs,files in os.walk(fn):
        for filename in fnmatch.filter(files,pattern):
            lb.insert('end',filename)


def pause_song():
    if pausebt["text"] == "Pause":
        mixer.music.pause()
        pausebt["text"] = "Play"
    else:
        mixer.music.unpause()
        pausebt["text"] = "Pause"


top = Frame(screen,bg="black")
top.pack(padx=15,pady=5,anchor='center')
lb1 = Label(screen,text="Music Player" ,font=("Apple LiGothic",20),fg="lightblue",bg="black").pack(in_=top,side="bottom")

button_explore = Button(screen,text = "Select music folder",font = ("Apple LiGothic",13),fg="lightblue",bg="black",command = searchFiles)                                                        
button_explore.pack(pady=(40,20))

lb = tk.Listbox(screen,fg = "lightblue",bg = "black",relief="solid",width =100 , font = ("Apple LiGothic",15))
lb.pack(padx=50)

control = Frame(screen,bg = "black")
control.pack(padx=15,pady=5,anchor='center')

prevbt = Button(screen,text = "Prev",bg = "black",fg="white",font = ("Apple LiGothic",10),image = prev_img,borderwidth=0,command=play_prev).pack(in_=control,padx=5,pady=10,side="left")
stopbt = Button(screen,text = "Stop",bg = "black",fg="white",font = ("Apple LiGothic",10),image = stop_img,borderwidth=0,command=stop).pack(in_=control,padx=5,pady=10,side="left")
pausebt = Button(screen,text = "Pause",bg = "black",fg="white",font = ("Apple LiGothic",10),image = pause_img,borderwidth=0,command=pause_song)
pausebt.pack(in_=control,padx=5,pady=10,side="left")
playbt = Button(screen,text = "Play",bg = "black",fg="white",font = ("Apple LiGothic",10),image = play_img,borderwidth=0,command=select).pack(in_=control,padx=5,pady=10,side="left")
nextbt = Button(screen,text = "Next",bg = "black",fg="white",font = ("Apple LiGothic",10),image = next_img,borderwidth=0,command=play_next).pack(in_=control,padx=5,pady=10,side="left")

currentsong = Label(screen,text='',bg = "black",fg='lightblue',font = ("Apple LiGothic",15))
currentsong.pack(pady=(25,25))

screen.mainloop()