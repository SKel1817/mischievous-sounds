import tkinter as tk
from tkinter import *
from playsound import playsound
from tkinter import filedialog
from PIL import Image, ImageTk
import os

#tkinter permaters
root = tk.Tk()
root.title("Mischievous Sounds")
root.geometry("640x480")

#set icon for window to icon.ico that is in sounds folder
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'sounds\\icon.ico'))
#set background color and make variables for button color
root['bg']='chartreuse4'
color = 'OliveDrab2'
color2 = 'khaki1'

def browseFiles():
    # open a file browser and find .wav files 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("WAV files", "*.wav*"), ("all files", "*.*")))
    # print it to the console
    print(filename)
    # make the button play the sound
    tk.Button(root, text="play custom sound", command = lambda:customsound1(filename),bg= color2,  width=20, height=3).grid(row=3, column=1)

def sound(num):
    #sound list
    sounds = ['zakariya_0_0.wav', 'mattcurtis_0_0.wav', 'sad.wav', 'alarm.wav', 'drum.wav','funny.wav']
    #makes num an int
    amount = int(num)
    #grabs the desired sound out of list
    play = sounds[amount]
    #grabs the sound from the sounds folder
    path = os.path.join(os.path.dirname(__file__), 'sounds\\' + play)
    #plays sound and makes sure it's an inte
    playsound(str(path))

def customsound1(name):
    #plays the custom sound
    playsound(name)

#title label
tk.Label(root, text="Mischievous Sounds", bg= 'chartreuse4', fg='white', font=('Helvetica', 20, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)

#sound buttons
#first row of buttons
tk.Button(root, text="classic implosion", command=lambda:sound('0'), bg= color, width=20, height=3).grid(row=1, column=0,padx=30, pady=30)
tk.Button(root, text="matt implosion", command=lambda:sound('1'), bg= color, width=20, height=3).grid(row=1, column=1,padx=30, pady=30)
tk.Button(root, text="sad music", command=lambda:sound('2'),  bg= color,width=20, height=3).grid(row=1, column=2,padx=30, pady=30)

#second row of buttons
tk.Button(root, text="alarm", command=lambda:sound('3'),bg= color,  width=20, height=3).grid(row=2, column=0,padx=30, pady=30)
tk.Button(root, text="drum", command=lambda:sound('4'), bg= color,width=20, height=3).grid(row=2, column=1,padx=30, pady=30)
tk.Button(root, text="alien?", command=lambda:sound('5'), bg= color,width=20, height=3).grid(row=2, column=2,padx=30, pady=30)

#file explorer button
button_explore = Button(root, text = "Browse Files to add custom sound",command = browseFiles, bg= color2, width=26, height=3).grid(row=4, column=0, pady=30)

#run tkinter
root.mainloop()