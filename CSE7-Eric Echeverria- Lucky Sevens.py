###
#sevens that are lucky
###

# Start with $10 every game cost $1 to play
# Roll two dice
# if the result is seven win $5 (+$4 overall after the cost of $1)
# the game continuously plays until you run out of money.
# At the end, it tells you how many rounds were played

import random 
money = 10
turn = 0
while money !=0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print "Your number is " + str(dice1+dice2)
    total = dice1 + dice2
    if total == 7:
        print "You win"
        money +=4
        print "Your money is: %d" % money
        turn += 1
    else:
        print "You Lose the round"
        money -=1
        print "Your money is: %d" % money
        turn += 1
print "Your total rounds  played were: %d" % turn
        
                  
        

    
    
            

    
    