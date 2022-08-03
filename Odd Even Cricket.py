#import random to compute random values from computer
import random as r

class odd_even():
    #there are two functions. one for setting the score and the other for chasing it
    def run_setter(self,z):
        #setting score for chaser to chase
        self.z=z
        #whether computer or user
        flag=True
        setter_score=0
        while flag==True:
            user_input=int(input('Your Number from 1,2,3,4,5,6->'))
            #taking input from user
            opponent_input=r.randint(1, 6)
            #taking number from opponent
            print('Opponent Number->',opponent_input)
            if user_input==opponent_input:
                #checking if score setter is out
                print('OUT!')
                flag=False
                break
            else:
                #checking the score setter playing is user or computer
                if z=='op':
                    setter_score=setter_score+opponent_input
                else:
                    setter_score=setter_score+user_input
                print(setter_score)
        final_setter_score=setter_score
        print('\nFinal score->',final_setter_score,'\n')
        return final_setter_score
        #returning final setter value for chaser
    
    
    def run_chaser(self,g,z):
        #chasing the score set by setter
        g=int(g)
        #final setter score
        self.z=z
        #whether computer or user
        flag=True
        chaser_score=0
        while flag==True:
            if g<chaser_score:
                #checking chaser score more than setter score
                flag=False
                break
            user_input=int(input('Your Number->'))
            #taking input from user
            opponent_input=r.randint(1, 6)
            #taking number from opponent
            print('Opponent Number->',opponent_input)
            if user_input==opponent_input:
                #checking if score chaser is out
                print('\nOUT!')
                flag=False
                break
            else:
                #checking the score setter playing is user or computer
                if z=='op':
                    chaser_score=chaser_score+opponent_input
                else:
                    chaser_score=chaser_score+user_input
                print(chaser_score)
        final_chaser_score=chaser_score
        print('\nFinal score->',final_chaser_score,'\n')
        #checking win conditions below
        if final_chaser_score>g and z=='op':
            print('\nOpponent Wins!')
        elif final_chaser_score>g and z!='op':
            print('\nYou Win!')
        elif final_chaser_score<g and z=='op':
            print('\nYou Win!')
        elif final_chaser_score<g and z!='op':
            print('\nOpponent Wins!')
        elif final_chaser_score==g:
            print('\nIts a Draw!')
    

    def rule(self):
        #Welcome message that also lays down the rules
        rule='''******Welcome to Odd Even Cricket Game******
        ->The objective of this game is to get more score than the opponent.
        ->Whichever player scores higher is declared the winner.
        ->All players start from 0.
        ->Toss is conducted between You and Opponent. Whoever wins get to choose the innings
        ->If you win, you may choose from batting or balling.
        ->You may enter any number between 1 to 6.
        ->If number entered by you and opponent is same, the player batting is declared OUT.
        ->All the Best!!!
        \n'''
        print(rule)


user=odd_even()
#calling the class in user object
user.rule()
choice=input('Heads or Tails->')
toss=r.randint(0, 1)
if toss==1:
    toss='Heads'
else:
    toss='Tails'
#toss heads or tails
if choice==toss:
    #user wins toss
    chosen=input('You won the toss.\nChoose batting or balling ->')
    if chosen=='batting':
        print('\nYour batting inning begins\n')
        a=user.run_setter('us')
        print('Your balling inning begins\n')
        user.run_chaser(a,'op')
    elif chosen=='balling':
        print('\nYour balling inning begins\n')
        b=user.run_setter('op')
        print('Your batting inning begins\n')
        user.run_chaser(b,'us')        
else:
    #computer wins toss
    print('You lost the toss\n')
    chosen=r.randint(0,1)
    if chosen==1:
        chosen='batting'
    else:
        chosen='balling' 
    if chosen=='batting':
        print('You lost the toss.\nOpponent chose batting')
        print('\nYour balling inning begins\n')
        c=user.run_setter('op')
        print('Your batting inning begins\n')
        user.run_chaser(c,'us')
    elif chosen=='balling':
        print('You lost the toss.\nOpponent chose balling')
        print('\nYour batting inning begins\n')
        d=user.run_setter('us')
        print('Your balling inning begins\n')
        user.run_chaser(d,'op')
print('\nThanks for playing')
