from time import sleep
from click import getchar
from random import randint
from os import system, _exit
from tqdm import tqdm
import colorama as co
from threading import Thread
# to use back space
trueAnswer = ture_ans = time = 0


def timer(): # Timer for 1 minute
    global time
    time = 60
    while time != 0:
        sleep(1)
        time -= 1
    system('cls')
    result(trueAnswer, ture_ans)


def delete(word): # Word Backspace
    if len(word) == 0:
        return ""
    # take apart the word
    lst = list(word)
    # delete the last letter
    lst.pop(-1)
    return "".join(lst)


def result(trueAnswer, ture_ans): # show the result of them game
    print(co.Fore.BLUE + "your speed type is <{}> word in minute and your accuracy : %{}".format(trueAnswer, int(ture_ans)))
    # print(ture_ans)
    if trueAnswer <= 15:
        print("you are slow need practice")
    if trueAnswer > 15 and trueAnswer <= 35:
        print("normal typing can be better")
    if trueAnswer > 35:
        print("well done you are perfect")
    _exit(0)


def starter():  # get acces to start program and start timer
    print(co.Style.BRIGHT + co.Fore.LIGHTGREEN_EX + " ")
    co.Fore.LIGHTGREEN_EX
    for i in tqdm(range(15), ncols=70):
        sleep(0.1)
    system("cls")
    print(co.Fore.BLUE + "Press Enter to start : ")
    while True:
        starter = getchar()
        if ord(starter) == 13:
            system('cls')
            Thread(target=timer).start()
            game()
        else:
            # just some thing for beauty
            for i in range(20):
                system('cls')
                sleep(0.001)
                print(co.Fore.BLUE + "Press Enter to start : ")


def game():  # main structer of game
    global trueAnswer, ture_ans
    trueAnswer = fail = all_w = 0
    lst = ["smoke", "struct", "mobile", "coding", "windows",
        "forward","smoke", "silver", "soldier", "stump", "google", 
        "linux", "pattern", "special", "mother", "language", "terminal", 
        "sandwich", "though", "enough", "might", "printer", "problem", "computer",
        "speak", "perhaps", "home", "book", "door", "think", "monster", "hello","good",
        "self", "night", "sun", "car", "at", "drive", "phone", "cost", "allow", "start",
        "type", "gold", "green", "sky", "home", "trust", "water", "what", "sleep", "cake",
         "freind", "programing", "level", "today", "search", "queen", "player", "game", "six",
          "seven", "movie", "music", "map", "while", "sound", "order", "number"]
    numb = []
    while True:
        # random get one of the words
        n = randint(0, (len(lst) - 2))
        # dont let come repetitious words
        if n not in numb:
            numb.append(n)
            print(co.Fore.GREEN + lst[n].ljust(10),
                  end=co.Fore.YELLOW + "|\tyour left time is : ")
            print(time, co.Fore.RED +
                  "\t\tyour true answers : {}".format(trueAnswer))
            word = ""
            while True:
                ch = getchar()
                # if put space end the procec
                if ch == " ":
                    system('cls')
                    break
                # 8 is codeaski of space in windows
                if ord(ch) == ord("\b"):
                    word = delete(word)
                    system('cls')
                    print(
                        co.Fore.GREEN + lst[n].ljust(10), end=co.Fore.YELLOW + "|\tyour left time is : ")
                    print(time, end=co.Fore.RED +
                          "\t\tyour true answers : {}\n".format(trueAnswer))
                    print(co.Fore.GREEN + word)
                else:
                    system('cls')
                    word += ch
                    print(
                        co.Fore.GREEN + lst[n].ljust(10), end=co.Fore.YELLOW + "|\tyour left time is : ")
                    print(time, end=co.Fore.RED +
                          "\t\tyour true answers : {}\n".format(trueAnswer))
                    print(co.Fore.GREEN + word)
            # trueAnswer all words that come
            all_w += 1
            # final check
            if word == lst[n]:
                trueAnswer += 1
            else:
                # count all wrong words
                fail += 1
            # find the porsant of true typing
            ture_ans = 100 - ((100 * fail) / all_w)


starter()