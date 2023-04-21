#import pygame

# #make a window
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Mischievous Sounds")

# button_size = width, height = 150, 100
# button_pos = x, y = 75, 250
# button = pygame.Rect(button_pos, button_size)
# #bilt button there
# screen.blit(button, button_pos)




# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#                 running = False
#                 quit()
#         pygame.display.update()

# if __name__ == '__main__':
#     main()

import tkinter as tk
from tkinter import*
from tkinter import messagebox
from playsound import playsound

root = tk.Tk()
root.title("Mischievous Sounds")
root.geometry("640x480")
sounds = ['zakariya_0_0.wav', 'mattcurtis_0_0.wav']
def play_sound():
    #play the zakariya_0_0.wav file
    # playsound(str(sounds[num]))
    playsound(sounds[0])
    #messagebox.showinfo("your sound has played")
def yikes():
    playsound('mattcurtis_0_0.wav')
def sound3():
    playsound('sad.wav')
    #messagebox.showinfo("your sound has played")
tk.Button(root, text="Play classic implosion", command=play_sound,  width=20, height=3).place(x=15, y=25)
#button0.pack(pady=20)
#button0.place(x=25, y=50)
tk.Button(root, text="play matt implosion", command = yikes,  width=20, height=3).place(x=250, y=25)
#button1.place(x=50, y=50)
tk.Button(root, text="play sad music", command = sound3,  width=20, height=3).place(x=450, y=25)


root.mainloop()