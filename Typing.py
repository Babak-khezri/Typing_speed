from time import sleep
from random import randint, shuffle
from threading import Thread
from tkinter import Tk, Label, Entry, PhotoImage, END, Button
from emojis import encode
from os import _exit
true_answers = word = number = 0
lst = ["smoke", "struct", "mobile", "coding", "windows", "forward", "smoke", "silver","soldier",
       "stump", "google", "linux", "pattern", "special", "mother", "language", "terminal","sandwich",
       "though", "enough", "might", "printer", "problem", "computer", "speak", "perhaps","home", "book",
       "door", "think", "monster", "hello", "good", "self", "night", "sun", "car", "at","drive", "phone",
       "what", "sleep", "cake", "freind", "program", "level", "today", "search", "queen", "player", "game",
       "six", "seven", "movie", "music", "map", "while", "sound", "order", "number", "voice", "site", "bomb",
       "pool", "head", "hand", "few", "alot", "smile", "python", "bad", "quiz", "want", "help", "change", "row",
       "cost", "allow", "start", "type", "gold", "green", "sky", "home", "trust", "water", "column", "light", "dark"]
shuffle(lst)  # Get random sorted list
win = Tk()
win.resizable(False, False)  # Lock change size
win.title('Typing speed')
app_icon = PhotoImage(
    file='C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\ico.png')
win.iconphoto(False, app_icon)  # Change icon
win['background'] = '#330066'  # Change main background
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
    show_word.config(text=lst[number], fg='#00e600',
                     font=(("Times", 32, 'bold')), bg='#330066')
    show_word.grid(row=1, column=1)
    show_true.config(text=true_answers, fg='red', font=(
        ("Times", 20, 'bold')), bg='#330066')
    show_true.grid(row=0, column=3)
    next_word.config(
        text="next = " + lst[number+1], fg='#ffff80', font=(("Times", 22, 'bold')), bg='#330066')
    next_word.grid(row=4, column=1)
    enter.delete(0, END)


def Get_word():
    global true_answers, number
    trueAnswer = 0
    while True:
        word_list = list(enter.get())
        sleep(0.01)  # Avoid from crush
        if len(word_list) != 0:
            if word_list[-1] == ' ':
                if "".join(word_list) == lst[number] + ' ':
                    true_answers += 1
                    number += 1
                else:
                    number += 1
                New_word()


def Timer():
    for time in range(60, -1, -1):
        show_time.config(text="time = " + str(time),
                         font=(("Times", 20, 'bold')), bg='#330066', fg='red')
        show_time.grid(row=0, column=0)
        sleep(1)
    win.withdraw()
    end()


def end():
    if number != 0: # Avoid from division by zero
        accuracy = 100 - ((100 * (number-true_answers)) / number)
    else:
        accuracy = 100
    text_1 = "Your speed type is <{}> word in minute".format(true_answers)
    text_2 = "Your accuracy is %{:.2f}".format(accuracy)
    if true_answers < 20:
        text_3 = "you are slow need practice"
        emoji = '😑'
    elif true_answers >= 20 and true_answers < 30:
        text_3 = "normal typing can be better"
        emoji = '🙂'
    else:
        text_3 = "well done you are perfect"
        emoji = '😊'

    score = Tk()
    score.resizable(False, False)  # Lock change size
    score.title('Scoreboard')
    score['background'] = '#ff99ff'  # Change main background
    Label(score, text=text_1, font=(("Times", 20, 'bold')), bg='#ff99ff').pack()
    Label(score, text=text_2, font=(("Times", 20, 'bold')), bg='#ff99ff').pack()
    Label(score, text=text_3, font=(("Times", 20, 'bold')), bg='#ff99ff').pack()
    Label(score, text=emoji, font=(("Times", 50, 'bold')), bg='#ff99ff').pack()
    Button(score, text='Exit', font=(("Times", 20, 'bold')),
           bd=16, bg='red', command=lambda: _exit(0)).pack()
    score.mainloop()


New_word()
Thread(target=Timer).start()
Thread(target=Get_word).start()
win.mainloop()
