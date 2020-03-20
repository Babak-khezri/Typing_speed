from time import time,sleep
from click import getchar
from random import randint
from os import system
from tqdm import tqdm
import colorama as co
# to use back space
def delete(word):
    if len(word) == 0:
        return ""
    #take apart the word
    lst = list(word)
    #delete the last letter
    lst.remove(lst[-1])
    # remake the word
    word = "".join(lst)
    return word
#show the result of them game
def result(trueAnswer,ture_ans):
    print( co.Fore.BLUE + "your speed type is : ",format(trueAnswer - 1)," word in minute and your accuracy : %",end=format(int(ture_ans)))
    #print(ture_ans)
    if trueAnswer <= 15 :
        print("\nyou are slow need practice")
    if trueAnswer > 15 and trueAnswer <= 35:
        print("\nnormal typing can be better")
    if trueAnswer > 35:
        print("\nwell done you are perfect") 
# get acces to start program and start timer
def starter():
    print(co.Style.BRIGHT + co.Fore.LIGHTGREEN_EX +  " ")
    co.Fore.LIGHTGREEN_EX
    for i in tqdm(range(15),ncols=70):
        sleep(0.1)
    system("cls")
    print(co.Fore.BLUE + "Press Enter to start : ")
    while True:
        starter = getchar()
        if ord(starter) == 13:
            system('cls')
            game()
        else:
            # just some thing for beauty
            for i in range(20):
                system('cls')
                sleep(0.001)
                print(co.Fore.BLUE + "Press Enter to start : ")
#main structer of game
def game():
    time_1 = time_2 = time()
    trueAnswer = fail = all_w = 0
    lst = ["smoke","struct","coding","windows","forward","smoke","silver","soldier","stump","google","linux","pattern","special","mother","language","terminal","sandwich","though","enough","might","printer","problem","computer","speak","perhaps","home","book","door","think","monster","hello","good","self","night","sun","car","at","drive","phone","cost","allow","start","type","gold","green","sky","home","trust","water","what","sleep","cake","freind","programing","level","today","search","queen","player","game","six","seven","movie","music","map","while","sound","order","number"]
    numb = []
    #get the number of words
    len_words = len(lst) - 1
    while (time_2 - time_1) < 60:
        #random get one of the words
        n = randint(0,(len_words-1))
        # dont let come repetitious words
        if n not in numb:
            numb.append(n)
            print(co.Fore.GREEN + lst[n].ljust(10),end = co.Fore.YELLOW + "|\tyour left time is : ")
            time_2 = time()
            print(int(60 -(time_2 - time_1)), co.Fore.RED + "\t\tyour true answers : {}".format(trueAnswer))
            word = ""
            ch = ''
            while True:
                ch = getchar()
                #if put space end the procec
                if ch == " ":
                    system('cls')
                    break
                # 8 is codeaski of space in windows
                if ord(ch) == ord("\b"):
                    word = delete(word)
                    system('cls')
                    print(co.Fore.GREEN + lst[n].ljust(10),end = co.Fore.YELLOW + "|\tyour left time is : ")
                    time_2 = time()
                    print(int(60 -(time_2 - time_1)),end = co.Fore.RED + "\t\tyour true answers : {}\n".format(trueAnswer))
                    print(co.Fore.GREEN +  word)
                else:
                    system('cls')
                    word += ch
                    print(co.Fore.GREEN + lst[n].ljust(10),end = co.Fore.YELLOW + "|\tyour left time is : ")
                    time_2 = time()
                    print(int(60 -(time_2 - time_1)),end = co.Fore.RED + "\t\tyour true answers : {}\n".format(trueAnswer))
                    print(co.Fore.GREEN +  word)
            #trueAnswer all words that come
            all_w += 1
            #final check
            if word == lst[n]:
                trueAnswer += 1
            else:
                #count all wrong words
                fail += 1
        time_2 = time()
    #find the porsant of true typing
    ture_ans = 100 - ((100 * fail) / all_w)
    result(trueAnswer,ture_ans)
starter()