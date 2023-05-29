#Shuffle Game Code
#Author Juneed Baba
#Date 29-05-2023
from random import shuffle

def shuffle_list(mylist):
    #take in mylist and return back shuffled list
    shuffle(mylist)
    return mylist

def guess_number():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('please enter your guess between 0,1,& 2')
    return int(guess)

def check_result(mylist,guess):
    if mylist[guess]=='0':
        print('Correct')
        print(mylist)
    else:
        print('wrong answer')
        print(mylist)
        
    
mylist = ['','0','']
shuffled = shuffle_list(mylist)
guess = guess_number()
check_result(shuffled,guess)
