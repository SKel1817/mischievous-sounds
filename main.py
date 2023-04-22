import tkinter as tk
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from tkinter import filedialog

#tkinter permaters

root = tk.Tk()
root.title("Mischievous Sounds")
root.geometry("640x480")
label_file_explorer = Label(root, text = "Submit your own sound", width = 100, height = 4, fg = "blue").place(x=150, y=380)
sounds = ['zakariya_0_0.wav', 'mattcurtis_0_0.wav']
def browseFiles():
    # open a file browser and find .wav files 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("WAV files", "*.wav*"), ("all files", "*.*")))
    # change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)
    print(filename)
    return filename  


def play_sound():
    #play the zakariya_0_0.wav file
    #playsound(str(sounds[num]))
    playsound('zakariya_0_0.wav')
    #messagebox.showinfo("your sound has played")
def yikes():
    playsound('mattcurtis_0_0.wav')
def sound3():
    playsound('sad.wav')
#def customsound1():
    #playsound()
    #messagebox.showinfo("your sound has played")

tk.Button(root, text="Play classic implosion", command=play_sound,  width=20, height=3).place(x=15, y=25)
#button0.pack(pady=20)
#button0.place(x=25, y=50)
tk.Button(root, text="play matt implosion", command = yikes,  width=20, height=3).place(x=250, y=25)
#button1.place(x=50, y=50)
tk.Button(root, text="play sad music", command = sound3,  width=20, height=3).place(x=450, y=25)

#button 3 but for custom sounds
#tk.Button(root, text="play custom sound", command = customsound1,  width=20, height=3).place(x=250, y=200)

#file explorer button
button_explore = Button(root, text = "Browse Files",command = browseFiles).place(x=320, y=400)

root.mainloop()