import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import pygame

#initialize pygame
pygame.mixer.init()

#tkinter permaters
root = tk.Tk()
root.title("Mischievous Sounds")
root.geometry("640x480")

#set icon for window to icon.ico that is in sounds folder
filepath = os.path.join(os.path.dirname(__file__), 'assets', 'icon.xbm')
root.iconbitmap('@' + filepath)
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
    tk.Button(root, text="play custom sound", command = lambda:customsound1(filename),bg= color2,  width=20, height=3).grid(row=5, column=1)

def sound(num):
    #sound list
    sounds = ['zakariya_0_0.wav', 'matt.wav', 'sad.wav', 'alarm.wav', 'drum.wav','funny.wav', 'ora.wav', 'punch.wav', 'val.wav','eli.wav','scream.wav','wahoo.wav']
    #makes num an int
    amount = int(num)
    #grabs the desired sound out of list
    play = sounds[amount]
    #grabs the sound from the sounds folder
    path = os.path.join(os.path.dirname(__file__), 'assets', play)
    #plays sound and makes using pygame
    #pygame.mixer.init()
    bruh = pygame.mixer.Sound(path)
    bruh.play()
    

def customsound1(name):
    #plays the custom sound using pygame
    bruh = pygame.mixer.Sound(name)
    bruh.play()

#title label
tk.Label(root, text="Mischievous Sounds", bg= 'chartreuse4', fg='white', font=('Helvetica', 20, 'bold')).grid(row=0, column=0, columnspan=3, pady=15)

#sound buttons
#first row of buttons
tk.Button(root, text="classic implosion", command=lambda:sound('0'), bg= color, width=20, height=3).grid(row=1, column=0,padx=15, pady=5)
tk.Button(root, text="implosion 2", command=lambda:sound('1'), bg= color, width=20, height=3).grid(row=1, column=1,padx=15, pady=5)
tk.Button(root, text="sad music", command=lambda:sound('2'),  bg= color,width=20, height=3).grid(row=1, column=2,padx=15, pady=5)

#second row of buttons
tk.Button(root, text="alarm", command=lambda:sound('3'),bg= color,  width=20, height=3).grid(row=2, column=0,padx=15, pady=5)
tk.Button(root, text="drum", command=lambda:sound('4'), bg= color,width=20, height=3).grid(row=2, column=1,padx=15, pady=5)
tk.Button(root, text="alien?", command=lambda:sound('5'), bg= color,width=20, height=3).grid(row=2, column=2,padx=15, pady=5)

#third row of buttons
tk.Button(root, text="ora", command=lambda:sound('6'), bg= color,width=20, height=3).grid(row=3, column=0,padx=15, pady=5)
tk.Button(root, text="punch", command=lambda:sound('7'), bg= color,width=20, height=3).grid(row=3, column=1,padx=15, pady=5)
tk.Button(root, text="imposion 3", command=lambda:sound('8'), bg= color,width=20, height=3).grid(row=3, column=2,padx=15, pady=5)

#fourth row of buttons
tk.Button(root, text="imposion 4", command=lambda:sound('9'), bg= color,width=20, height=3).grid(row=4, column=1,padx=15, pady=5)
tk.Button(root, text="Scream", command=lambda:sound('10'), bg= color,width=20, height=3).grid(row=4, column=0,padx=15, pady=5)
tk.Button(root, text="Wahoo", command=lambda:sound('11'), bg= color,width=20, height=3).grid(row=4, column=2,padx=15, pady=5)




#file explorer button
button_explore = Button(root, text = "Browse Files to add custom sound",command = browseFiles, bg= color2, width=26, height=3).grid(row=6, column=0, pady=5)

#run tkinter
root.mainloop()