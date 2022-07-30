import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("CSK Music Player")
canvas.geometry("600x800")
# Add image file
bg = tk.PhotoImage( file = "wallpaperfin.png")
# Show image using label
label1 = tk.Label( canvas, image = bg)
label1.place(x = 0,y = 0)
# Add text
label2 = tk.Label( canvas, text = "Enjoy The Music", bg = "#88cffa")
label2.pack(pady = 50)
# Create Frame
frame1 = tk.Frame(canvas, bg = "#88cffa")
frame1.pack(pady = 20)
canvas.mainloop()
