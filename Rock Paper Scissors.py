#import random to compute random values from computer
import random as r
def play():
    ys=0
    #your score
    cs=0
    #computer score
    s=0
    #total turns
    while(s<5):
        choice=input('Enter your choice: Rock:r /Paper:p /Scissor:s : ')
        #you enter your choice
        computer_choice=r.sample(('r','p','s'),k=1)
        #computers choice from rock,paper,scissor
        y=choice
        c=''.join(computer_choice)
        #converting choice from list to char
        if y==c:
            #if both choices are same
            print("Computer Choice: ",c)
            print("Point goes to no one")
            s+=1
        elif y=='r':
            if c=='s':
                print("Computer Choice: ",c)
                print("Point goes to You")
                ys+=1
                s+=1
            else:
                print("Computer Choice: ",c)
                print("Point goes to Computer")
                cs+=1
                s+=1
        elif y=='p':
            if c=='r':
                print("Computer Choice: ",c)
                print("Point goes to You")
                ys+=1
                s+=1
            else:
                print("Computer Choice: ",c)
                print("Point goes to Computer")
                cs+=1
                s+=1
        elif y=='s':
            if c=='p':
                print("Computer Choice: ",c)
                print("Point goes to You")
                ys+=1
                s+=1
            else:
                print("Computer Choice: ",c)
                print("Point goes to Computer")
                cs+=1
                s+=1
        else:
            #in case of unvalid ipnut
            print("Enter valid choice")
        print("Score: You:",ys," Computer:",cs)
    print("Final Score: You:",ys," Computer:",cs)
    #print final score
    print("You Win!") if ys>cs else print("Computer Wins!")
    #print winner

q='''************ Rock Paper Scissors ************
Welcome to Rock-Paper-Scissor.
You will play for 5 turns.
The rules are simple:
Scissor beats Paper.
Paper beats Rock.
Rock beats Scissor.
Enter your choice as r for rock, p for paper, s for scissor.
*______________________*'''
#rules
print(q)
play()
print("Thanks for Playing!!!")