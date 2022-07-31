import random as r


class snakes_and_ladder():
    def movement(self,_current_position):
        n=snakes_and_ladder()
        #object of class is created to access other function of the class
        print('Initial Position',_current_position)
        dice=r.randint(1, 6)
        #rolling of dice
        print('Dice ',dice)
        _current_position=_current_position+dice
        if _current_position>100:
            #if player in cell 94 and above, dice roll is negated if the sum exceeds 100
            print('Dice cannot be added')
            print('Interim Position ',_current_position-dice)
            print('Final Position ',_current_position-dice)
            print('\n')
            _current_position=_current_position-dice
            return _current_position
        print('Interim Position ',_current_position)
        _current_position=n.check_cell(_current_position)
        #checking current cell for either snakes or ladders
        print('Final Position ',_current_position)
        print('\n')
        a=_current_position
        return a


    def check_cell(self,_new_cell_):
        #checking position of ladders and snakes from set defined outside class
        if _new_cell_ in ladder.keys():
            _new_cell_=_new_cell_+ladder.get(_new_cell_)
            #adding the value of ladder into current position
            return _new_cell_
        elif _new_cell_ in snakes.keys():
            _new_cell_=_new_cell_-snakes.get(_new_cell_)
            #substracting the value snake from current position
            return _new_cell_
        else:
            #no change made to position when no ladder or snake is in the cell
            return _new_cell_
    
    
    def rules(self):
        #Welcome message that also lays down the rules
        rules='''************Welcome to Snakes and Ladders.************
        ->The objectiove of this game to reach the 100th cell.
        ->Whichever player reaches the position first is declared the winner.
        ->All players start at 0th cell.
        ->Ladders and snakes have been placed at various cells throughout the board.
        ->If you step on ladder then you go forwards.
        ->If you step on snake then you go backwards.
        ->Initial Position is your starting cell.
        ->Dice is the number acquired after rolling of dice.
        ->Interim Position is the position after adding dice to initial position.
        ->Final Position is the position after checking for snakes or ladders on interim position. 
        ->All the Best!!!
        \n'''
        print(rules)
    
    
ladder={1:37,4:10,9:22,21:21,28:56,51:16,72:19,80:19}
#the positions of ladders followed by the value to be incremented
snakes={17:10,54:20,62:43,64:4,87:36,93:20,95:20,98:19}
#the positions of snakes followed by the value to be decremented
player1=snakes_and_ladder()
#creating player1
player2=snakes_and_ladder()
#creating pllayer2
snakes_and_ladder().rules()
player1._current_position=0
#setting initial value to 0
player1.z='Red'
#assigning color to player1
player2._current_position=0
#setting initial value to 0
player2.z='Blue'
#assigning color to player2


while player1._current_position!=100 or player2._current_position!=100:
    #loop functions until either value reaches 100
    print(player1.z)
    b=player1.movement(player1._current_position)
    player1._current_position=b
    if player1._current_position==100:
        #player1 reaches 100 and loop terminates
        print(f'Congratulations {player1.z}!!You are the winner.')
        break
    print(player2.z)
    #player2 gets turn after player1
    h=player2.movement(player2._current_position)
    player2._current_position=h
    if player2._current_position==100:
        #player2 reaches 100 and loop terminates
        print(f'Congratulations {player2.z}!!You are the winner.')
        break


print('Thanks for playing this game.')