
#Implementation of Tic-Tac-Toe game in Python.

#The Board is made using dictionaries in Python

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

#print the updated board

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("Your turn," + turn + ".Make your move")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Can't move!It's filled.\nMake other move?")
            continue

        # Check who wins
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " Won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If nobody wins then display as tie
        if count == 9:
            print("\nGame Over.\n")                
            print("Nobody wins!Tie!!")

        # For changing the players after a move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #Restarting the game or not
    game_restart = input("Want to play Again?(y/n)")
    if game_restart== "y" or game_restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
