
# coding: utf-8

# In[ ]:


# Connect4.py

# This is the controller in the model-view-controller pattern.

# Users take turns dropping pieces in a 6 x 7 board.  Pieces fall to the lowest
# open space.  Whoever gets 4 of their pieces in a row vertically, horizontally,
# or diagonally wins the game.  The Java implementation uses a 2D array to
# represent the empty spaces of the grid.
 
# by Evan Morgan

ROWS = 6;            # Board height
COLS = 7;            # Board width
EMPTY = '.';        # Indicate empty place
CHECKER0 = 'X';     # Indicate the first player's checker
CHECKER1 = 'O';     # Indicate second player's checker
CHECKERS = [CHECKER0, CHECKER1]

class Connect4(object):
    
    def __init__(self):
        """
        Main method to run the Connect 4 game. Prompts user for player names to
        determine human or computer player. When game ends, winner is displayed.
        """
        view = Connect4ViewText()

        # Initialize the game 
        players = [self.makePlayer(view, "first"), self.makePlayer(view, "second")]

        # Hold current game state
        state = Connect4Game(0, players)  

        view.display(state)

        while(not state.gameIsOver()):
            move = state.getPlayerToMove().getMove(state, view)
            state.makeMove(move)
            print("Static evaluator value: " + str(state.staticEvaluator()))
            view.display(state)

        winnerNum = 1 - state.getPlayerNum()
        view.reportToUser(players[winnerNum].getName() + " wins!")

    def makePlayer(self, view, playerMsg):
        """
        Method to create a Connect 4 player using a name from user input.
        If name contains phrase "Computer," the player produced is a computer.
        """
        playerName = view.getAnswer("Enter the name of the " + playerMsg + 
                " player." + "\n(Include 'Computer' in the name of a computer player) ")
        if("Computer" in playerName):
            depth = view.getIntAnswer("How far should I look ahead? ")
            return ComputerConnect4Player(playerName, depth)
        else:
            return HumanConnect4Player(playerName)

