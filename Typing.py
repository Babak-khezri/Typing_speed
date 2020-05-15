from time import sleep
from click import getchar
from random import randint
from os import system, _exit
import colorama as co
from threading import Thread
from tkinter import *
word = None
time_pass = 60
true_answers = 0
lst = ["smoke", "struct", "mobile", "coding", "windows","forward","smoke", "silver", "soldier", "stump", "google","linux", "pattern", "special", "mother", "language", "terminal", "sandwich", "though", "enough", "might", "printer", "problem", "computer","speak", "perhaps", "home", "book", "door", "think", "monster", "hello","good","self", "night", "sun", "car", "at", "drive", "phone", "cost", "allow", "start","type", "gold", "green", "sky", "home", "trust", "water", "what", "sleep", "cake","freind", "programing", "level", "today", "search", "queen", "player", "game", "six","seven", "movie", "music", "map", "while", "sound", "order", "number"]
win = Tk()
win.resizable(False,False) # Lock change size
win.title('Typing speed')
app_icon = PhotoImage(file = 'C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
win.iconphoto(False , app_icon) # Change icon
win['background']='#000d33' # Change main background
win.geometry('700x500')

def new_word():
    global word , true_answers
    word = lst[randint(0,len(lst)-2)]
    show_word.config(text=word,fg='red',font=(("Times",32,'bold')),bg='#000d33')
    show_word.place(x=10,y=50)
    show_true.config(text=true_answers,fg='red',font=(("Times",32,'bold')),bg='#000d33')
    show_true.place(x=20,y=70)
    enter.delete(0, END)
    enter.insert(0, "")
show_word = Label(win)
show_true = Label(win)
enter = Entry(win)
enter.config(font = ("Aryal",32,'bold'),bg = "pink")
enter.place(x=60,y=85)
show_time = Label(win)
new_word()
def Get_word():
    global word , true_answers
    trueAnswer = 0 
    while True:
        word_list = list(enter.get())
        sleep(0.01)
        if len(word_list) != 0:
                if word_list[-1] == ' ':
                    if "".join(word_list) == word + ' ':
                        true_answers += 1
                    new_word()
def Timer():
    time = 60
    while True:
        show_time.config(text="time = " + str(time),font=(("Times",32,'bold')),bg='#000d33',fg='red')
        show_time.place(x=50,y=80)
        time -= 1
        if time == 0:
            win.destroy()
            end()
        sleep(1)
def end():
    tkin = Tk()
    tkin.mainloop()

Thread(target=Timer).start()
Thread(target=Get_word).start()
win.mainloop()