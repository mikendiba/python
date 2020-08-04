from tkinter import *
from tkinter import filedialog
from pygame import mixer




root = Tk()

menubar = Menu(root)
root.config(menu = menubar)

submenu = Menu(menubar,tearoff = 0)
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


menubar.add_cascade(label ="File",menu = submenu)
submenu.add_command(label ="Open", command = browse_file)
submenu.add_command(label ="Exit",command = root.destroy)

submenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label ="Help",menu = submenu)
submenu.add_command(label ="About Us")


mixer.init()

root.geometry('400x300')
root.title('Musicana')
root.iconbitmap(r'Musicana.ico')
text = Label(root,text = "Lets play Some Music!").pack()
def play_music():
        mixer.music.load(filename)
        mixer.music.play()


def stop_music():
     mixer.music.stop()

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


Playphoto = PhotoImage(file = 'Play.png')
labelphoto =Label(root, image = Playphoto).pack()
Playbtn = Button(root, text = "Play", command = play_music).pack()

Stopbtn = Button(root,text = "Pause",command = stop_music).pack()

scale = Scale(root, from_=0, to =100, orient = HORIZONTAL, command = set_vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.pack()


root.mainloop()