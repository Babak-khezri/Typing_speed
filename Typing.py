from time import *
from click import *
from random import *
from os import *
import colorama as col
# to use back space
def delete(word):
    x = (len(word))
    if x == 0:
        return ""
    lst = []
    # put the letters of a word in list
    for i in range(x):
        lst.append(word[i])
    #delete the last letter
    lst.pop(x-1)
    word = ""
    # remake the word
    for i in lst:
        word += i
    return word
# get acces to start program and start timer
def result(count,ture_ans):
    print( col.Fore.BLUE + col.Style.BRIGHT + "your speed type is : ",format(count - 1)," word in minute and your accuracy : %",end=format(int(ture_ans)))
    #print(ture_ans)
    if count <= 15 :
        print("\nyou are slow need practice")
    if count > 15 and count <= 35:
        print("\nnormal typing can be better")
    if count > 35:
        print("\nwell done you are perfect") 
def starter():
    print(col.Style.BRIGHT + col.Fore.BLUE + "Press Enter to start : ")
    while True:
        starter = getchar()
        if ord(starter) == 13:
            system('cls')
            break
        else:
            # just some thing for beauty
            for i in range(20):
                system('cls')
                sleep(0.001)
                print(col.Style.BRIGHT + col.Fore.BLUE + "Press Enter to start : ")
starter()
time_1 = time_2 = time()
count = fail = all_w = 0
lst = ["smoke","struct","coding","windows","forward","smoke","silver","soldier","stump","google","linux","pattern","special","mother","language","terminal","sandwich","though","enough","might","printer","problem","computer","speak","perhaps","home","book","door","think","monster","hello","good","self","night","sun","car","at","drive","phone","cost","allow","start","type","gold","green","sky","home","country","water","what","sleep","cake","freind","programing","level","today","search","queen","player","game","six","seven","movie","music","map","while","sound","order","number"]
numb = []
#get the number of words
len_words = len(lst) - 1
while (time_2 - time_1) < 60:
    #random get one of the words
    n = randint(0,(len_words-1))
    # dont let come repetitious words
    if n not in numb:
        numb.append(n)
        print(col.Fore.GREEN + col.Style.BRIGHT + lst[n], col.Fore.YELLOW + col.Style.BRIGHT +  "\t|\tyour left time is : ",end="")
        time_2 = time()
        print(int(60 -(time_2 - time_1)), col.Fore.RED + col.Style.BRIGHT + "\t\tyour true answers : {}".format(count))
        word = ""
        ch = ''
        while True:
            ch = getchar()
            if ch == " ":
                system('cls')
                break
            if ord(ch) == 8: # 8 is codeaski of space in windows
                word = delete(word)
                system('cls')
                print(col.Fore.GREEN + col.Style.BRIGHT + lst[n],end = col.Fore.YELLOW + col.Style.BRIGHT +  "\t|\tyour left time is : ")
                time_2 = time()
                print(int(60 -(time_2 - time_1)),end = col.Fore.RED + col.Style.BRIGHT + "\t\tyour true answers : {}\n".format(count))
                print(col.Fore.GREEN + col.Style.BRIGHT +  word)
            else:
                system('cls')
                word += ch
                print(col.Fore.GREEN + col.Style.BRIGHT + lst[n],end = col.Fore.YELLOW + col.Style.BRIGHT + "\t|\tyour left time is : ")
                time_2 = time()
                print(int(60 -(time_2 - time_1)),end = col.Fore.RED + col.Style.BRIGHT + "\t\tyour true answers : {}\n".format(count))
                print(col.Fore.GREEN + col.Style.BRIGHT +  word)
        #count all words that come
        all_w += 1
        #final check
        if word in lst:
            count += 1
        else:
            #count all wrong words
            fail += 1
    time_2 = time()
ture_ans = 100 - ((100 * fail) / all_w)
result(count,ture_ans)