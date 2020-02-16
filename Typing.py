from time import *
from click import *
from random import *
from os import *
def delete(word):
    x = (len(word))
    if x == 0:
        return ""
    lst = []
    for i in range(x):
        lst.append(word[i])
    lst[x-1] = ""
    word = ""
    for i in lst:
        word += i
    return word
print("Press Enter to start : ")
while 1:
    starter = getchar()
    if ord(starter) == 13:
        system('clear')
        break
    else:
        for i in range(20):
            system('clear')
            sleep(0.001)
            print("Press Enter to start : ")
time_1 = time()
time_2 = time()
count = 0
lst = ["smoke","struct","coding","windows","pattern","special","terminal","sandwich","though","enough","might","printer","problem","computer","speak","perhaps","home","book","door","think","monster","hello","good","self","night","sun","car","at","drive","phone","cost","allow","start","type","gold","green","sky","home","country","water","what","sleep","cake","freind","programing","level","today","search","queen","player","game","six","seven","movie","music","map","while","sound","order","number"]
numb = []
len_words = len(lst) - 1
while (time_2 - time_1) < 60:
    n = randint(0,(len_words-1))
    if n not in numb:
        numb.append(n)
        print(lst[n],end = "   |   your left time is : ")
        print(int(60 -(time_2 - time_1)),end = "        your true answers : ")
        print(count)
        word = ""
        ch = ''
        while 1:
            ch = getchar()
            if ch == " ":
                system('clear')
                break
            if ord(ch) == 127:
                word = delete(word)
                system('clear')
                print(lst[n],end = "   |   your left time is : ")
                print(int(60 -(time_2 - time_1)),end = "        your true answers : ")
                print(count)
                print(word)
            else:
                system('clear')
                word += ch
                print(lst[n],end = "   |   your left time is : ")
                print(int(60 -(time_2 - time_1)),end = "        your true answers : ")
                print(count)
                print(word)
        if word in lst:
            count += 1
    time_2 = time()
print("your speed type is : ",format(count)," word in minute")
if count <= 15 :
    print("you are slow need practice")
if count > 15 and count <= 35:
    print("normal typing can be better")
if count > 35:
    print("well done you are perfect") 