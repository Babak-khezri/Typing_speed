from time import *
from click import *
from random import *
from os import *
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
    lst[x-1] = ""
    word = ""
    # remake the word
    for i in lst:
        word += i
    return word
# get acces to start program and start timer
print("Press Enter to start : ")
while True:
    starter = getchar()
    if ord(starter) == 13:
        system('clear')
        break
    else:
        # just some thing for beauty
        for i in range(20):
            system('clear')
            sleep(0.001)
            print("Press Enter to start : ")
time_1 = time()
time_2 = time()
count = 0
fail = 0
all_w = 0
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
        print(lst[n],  "   |   your left time is : ",end="")
        print(int(60 -(time_2 - time_1)), "        your true answers : {}".format(count))
        word = ""
        ch = ''
        while True:
            ch = getchar()
            if ch == " ":
                system('clear')
                break
            if ord(ch) == 127: # 127 is codeaski of space
                word = delete(word)
                system('clear')
                print(lst[n],end = "    |   your left time is : ")
                print(int(60 -(time_2 - time_1)),end = "         your true answers : {}\n".format(count))
                print(word)
            else:
                system('clear')
                word += ch
                print(lst[n],end = "    |   your left time is : ")
                print(int(60 -(time_2 - time_1)),end = "         your true answers : {}\n".format(count))
                print(word)
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
print("your speed type is : ",format(count)," word in minute and your accuracy : %",end=format(int(ture_ans)))
#print(ture_ans)
if count <= 15 :
    print("\nyou are slow need practice")
if count > 15 and count <= 35:
    print("\nnormal typing can be better")
if count > 35:
    print("\nwell done you are perfect") 