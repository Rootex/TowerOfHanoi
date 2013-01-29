# This game is an experimental implemetatio of
# Tower of hanoi create by Sotaya Yakubu 
# Plaix inc.
#
# This software can be copied for the purpose
# of improvement, modification or experimentation
# For any commercial use, an agreement have to be
# sign between developer and second pathy.
#
# For contact reasons:
# Developer: Sotaya Yakubu
# Email: sotayamy@yahoo.co.uk
#
# For more details on software check the 
# README file in the main repository


################################################


class HanoiLevelOne(object):
    #disks = {"red":2, "blue": 4, "green": 6}
    #initializing rods, which never change
    #red=2
    #blue=4
    #green=6
    
    rod1 = []
    rod2 = []
    rod3 = []
    noOfMoves = 0
    
    #we always initialize all disks into first rod
    def __init__(self):
        self.rod1 = [6, 4, 2]
    
    #moves, when player tries to move disks from one rod to another
    #i am implementing a stack, so i can easily pop top element and compare
    
    def moves(self, origin,  destination):
        if len(origin) == 0:#you can't move anything from an empty stack
            print "There are no disks in this Origin"
        
        #checking if destination is empty, if true move element else check which is greater
        else:
            if len(destination) == 0:
                destination.append(origin.pop())
            elif destination[len(destination)-1] > origin[len(origin)-1]:
                destination.append(origin.pop())
            else:
                print "You are not allowed to make that move"
        self.noOfMoves+=1
        
    #the lowest number of moves required to complete game    
    #def perfectScore(self):
     #   return (2 ** 3) - 1
    
    #level completion with score
    def levelOneComplete(self):
        if len(self.rod3) == 3 and self.noOfMoves == self.perfectScore:
            print "Level One Complete with Perfect Score "+str(self.noOfMoves)
            return True
        
        elif len(self.rod3) == 3 and self.noOfMoves != self.perfectScore:
            print "Level One cComplete with score "+str(self.noOfMoves)+\
            " You can complete this level in "+str(self.perfectScore)+" moves"
            return True
        
        else:
            print "Level not complete"
            return False

#initialization of level
game1 = HanoiLevelOne()
perfectScore = (2**3)-1
print game1.rod1
#game on till level completion
while True:
    try:
        origin = int(raw_input("Input Origin(1, 2, 3): "))
        destination = int(raw_input("Input Destination(1, 2, 3): "))
        if origin == 1 and destination == 2:
            game1.moves(game1.rod1, game1.rod2)
            
        elif origin == 1 and destination == 3:
            game1.moves(game1.rod1, game1.rod3)
            
        elif origin == 2 and destination == 1:
            game1.moves(game1.rod2, game1.rod1)
            
        elif origin == 2 and destination == 3:
            game1.moves(game1.rod2, game1.rod3)
        
        elif origin == 3 and destination == 1:
            game1.moves(game1.rod3, game1.rod1)
            
        elif origin == 3 and destination == 2:
            game1.moves(game1.rod3, game1.rod2)
        
        elif origin == 1 and destination == 1:
            game1.moves(game1.rod1, game1.rod1)
            
        elif origin == 2 and destination == 2:
            game1.moves(game1.rod2, game1.rod2)
        
        elif origin == 3 and destination == 3:
            game1.moves(game1.rod3, game1.rod3)
            
        else:
            print "Move not valid"    
        
        print game1.rod1
        print game1.rod2
        print game1.rod3
        
        if len(game1.rod3) == 3 and game1.noOfMoves == perfectScore:
            print "Level One Complete with Perfect Score "+str(game1.noOfMoves)
            break;
        
        elif len(game1.rod3) == 3 and game1.noOfMoves != perfectScore:
            print "Level One cComplete with score "+str(game1.noOfMoves)+\
            " You can complete this level in "+str(perfectScore)+" moves"
            break;
            
    except Exception as detail:
        print "Unexpected error: ", detail
#game1.levelOneComplete
