from time import sleep
from random import randint, shuffle
from threading import Thread
from tkinter import Tk, Label, Entry, PhotoImage, END
true_answers = word = number = 0
lst = (["smoke", "struct", "mobile", "coding", "windows", "forward", "smoke", "silver", "soldier", "stump", "google", "linux", "pattern", "special", "mother", "language", "terminal", "sandwich", "though", "enough", "might", "printer", "problem", "computer", "speak", "perhaps", "home", "book", "door", "think", "monster", "hello","good", "self", "night", "sun", "car", "at", "drive", "phone", "cost", "allow", "start", "type", "gold", "green", "sky", "home", "trust", "water", "what", "sleep", "cake", "freind", "programing", "level", "today", "search", "queen", "player", "game", "six", "seven", "movie", "music", "map", "while", "sound", "order", "number"])
shuffle(lst) # Get random sorted list
win = Tk()
win.resizable(False, False)  # Lock change size
win.title('Typing speed')
app_icon = PhotoImage(file='C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
win.iconphoto(False, app_icon)  # Change icon
win['background'] = '#ff8080'  # Change main background
win.geometry('484x220')
show_word = Label(win)
next_word = Label(win)
show_true = Label(win)
enter = Entry(win)
enter.config(font=("Aryal", 32, 'bold'), bg="pink")
enter.grid(row=3, column=0, columnspan=5)
show_time = Label(win)


def New_word():
    global true_answers, number
    show_word.config(text=lst[number], fg='red', font=(("Times", 32, 'bold')), bg='#ff8080')
    show_word.grid(row=1, column=1)
    show_true.config(text=true_answers, fg='red', font=(("Times", 20, 'bold')), bg='#ff8080')
    show_true.grid(row=0, column=3)
    next_word.config(text="next = " + lst[number+1], fg='red', font=(("Times", 22, 'bold')), bg='#ff8080')
    next_word.grid(row=4, column=1)
    enter.delete(0, END)
    number += 1


def Get_word():
    global true_answers, number
    trueAnswer = 0
    while True:
        word_list = list(enter.get())
        sleep(0.01)  # Avoid from crush
        if len(word_list) != 0:
            if word_list[-1] == ' ':
                if "".join(word_list) == lst[number-1] + ' ':
                    true_answers += 1
                New_word()


def Timer():
    for time in range(60, -1, -1):
        show_time.config(text="time = " + str(time),font=(("Times", 20, 'bold')), bg='#ff8080', fg='red')
        show_time.grid(row=0, column=0)
        sleep(1)
    win.withdraw()
    end()


def end():
    tkin = Tk()
    tkin.mainloop()

New_word()
Thread(target=Timer).start()
Thread(target=Get_word).start()
win.mainloop()
