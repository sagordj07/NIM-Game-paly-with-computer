
import random

num = 0
ston = 0
pile = 0
stones = 0
piles = 0

def main():
    rockList = []
    randPile = 4
    randRock = 4
    print(randPile  , ' ' , randRock)
    name1, name2 = get_players()

    player = name1 
    
    get_board(rockList, randPile, randRock, player)

    play_again(rockList, randPile, randRock, name1, name2, player) 

def get_players():
    return input("Enter player 1 name: "), input("Enter player 2 name: ")

def get_board(rockList, randPile, randRock, player):

    print("Let's look at the board now.")
    print("-" * 25)
    for i in range(0, randPile):
        randRock = random.randint(1, 8)
        print('Pile {}: {}'.format(i + 1, 'O' * randRock))
        rockList.append(randRock)
    print("-" * 25)

    nim_sum(rockList, randPile)

def get_valid_input(rockList, randPile, player):
    global num
    while True:
        if(num % 2 == 0):
            print(' My Turn : ')
            stones = int(input('{}, how many stones to remove? '.format(player)))
            piles = int(input('Pick a pile to remove from: '))
        else:
            print('Computer Turn : ')
            stones = ston
            piles = pile
            print(stones , ' remomved from ' , pile , ' number pile By computer')

        if (stones and piles):
            if (int(stones) > 0) and (int(piles) <= len(rockList)) and (int(piles) > 0):
                if (int(stones) <= rockList[int(piles) - 1]):
                    if (int(stones) != 0) and (int(piles) != 0):
                        num = num + 1
                        break
        
        print("Hmmm. You entered an invalid value. Try again, {}.".format(player))
        
    # Update state
    rockList[int(piles) - 1] -= int(stones)

    # Keep playing game
    continue_game(rockList, randPile, player)

def continue_game(rockList, randPile, player): 
    print("Let's look at the board now.")
    print("-" * 25)
    for i in range(0, randPile):
        print("Pile {}: {}".format(i + 1, 'O' * rockList[i]))

    print("-" * 25)

    if rockList != [0] * len(rockList):
        nim_sum(rockList, randPile)


def play_again(rockList, randPile, randRock, name1, name2, player):

    while True:
        get_valid_input(rockList, randPile, player)
        
        # To determine winner, check if rockList contains all 0's on that player's turn
        if rockList == [0] * len(rockList):
            print("{} is the winner of this round!".format(player))
            user = input("Do you want to play again? Enter y for yes, anything for no: ")

            if user.lower() == 'y':
                # reset all conditions, start the game again
                rockList = []
                randPile = random.randint(2, 5)
                name1, name2 = get_players()
                player = name1
                get_board(rockList, randPile, randRock, player)
                get_valid_input(rockList, randPile, player)
                
            else:
                break
            
        # switch players 2->1, 1->2 
        if player == name1:
            player = name2

        else:
            player = name1

# Pre : accepts modified rockList, random integer for piles
# Post: calculates nim sum and prints the computer hint for optimal moves
def nim_sum(rockList, randPile):
    nim = 0
    global ston
    global pile
    # Calculate nim sum for all elements in the rockList
    for i in rockList:
        nim = nim ^ i
        
    print("Hint: nim sum is {}.".format(nim))

    # Determine how many rocks to remove from which pile
    stones_to_remove = max(rockList) - nim
    stones_to_remove = abs(stones_to_remove)    

    # Logic for certain configurations on determining how many stones to remove from which pile
    # "rockList.index(max(rockList))+ 1 )" determines the index in rockList at which the biggest
    # pile of stones exists.
    if (nim > 0) and (len(rockList) > 2) and (nim != max(rockList)) and (nim !=1):
        #print("Pick {} stones from pile {}".format(stones_to_remove, rockList.index(max(rockList))+ 1 ))
        ston = stones_to_remove
        pile = rockList.index(max(rockList))+ 1
        #print( ston , ' No ' , pile)

    if (nim > 0) and (len(rockList) > 2) and (nim == max(rockList)) and (nim !=1):
        ston = nim
        pile = rockList.index(max(rockList))+ 1
        #print( ston , ' No ' , pile)
        #print("Pick {} stones from pile {}.".format(nim, rockList.index(max(rockList))+ 1 ))

    if nim > 0 and len(rockList) <= 2 and (stones_to_remove != 0):
        ston = stones_to_remove
        pile = rockList.index(max(rockList))+ 1
        #print( ston , ' No ' , pile)
        #print("Pick {} stones from pile {}".format(stones_to_remove, rockList.index(max(rockList))+ 1 ))

    if nim > 0 and len(rockList) <= 2 and (stones_to_remove == 0):
        ston = nim
        pile = rockList.index(max(rockList))+ 1
       # print( ston , ' No ' , pile)
       # print("Pick {} stones from pile {}".format(nim, rockList.index(max(rockList))+ 1 ))

    elif (nim == 1) and (len(rockList) <= 2):
        ston = nim
        pile = rockList.index(max(rockList))+ 1
       # print( ston , ' No ' , pile)
       # print("Pick {} stones from pile {}".format(nim, rockList.index(max(rockList))+ 1 ))

    if (nim == 1) and (nim == max(rockList)) and (nim != 0) and (len(rockList) > 2):
        ston = nim
        pile = rockList.index(max(rockList))+ 1
        #print( ston , ' No ' , pile)
        #print("Pick {} stones from pile {}".format(nim, rockList.index(max(rockList))+ 1))
        
    if nim == 0:
        ston = rockList[rockList.index(max(rockList))]
        pile = rockList.index(max(rockList))+ 1
        #print( ston , ' No ' , pile)
        #print("Pick all stones from pile {}.".format(rockList.index(max(rockList))+ 1 ))

main()
    
