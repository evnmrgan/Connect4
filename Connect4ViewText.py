
# coding: utf-8

# In[ ]:


# A text implementation of the "view" part of a model-view-controller 
# version of Connect 4. Used to test various runs and conditions 

class Connect4ViewText():

    def __init__(self):
        pass
    
    def display(self, state):
        """
        Method to represent the Connect4 board using text
        """
        board = state.getBoard()
        print()
        print('   '.join(map(lambda row: str(row), range(COLS-1))))
        for row in reversed(range(0,ROWS)):
            print('   '.join(board[row][col] for col in range(ROWS)))
                   
    def getUserMove(self, state):
        """
        Method to ask for the player's move and check if it's valid
        """
        print()
        col = self.getIntAnswer("Which column to place checker, " + state.getPlayerToMove().getName() + "? ")
        while (not state.isValidMove(col)):
            col = self.getIntAnswer("Column to place checker? ")
        return col

    def reportMove (self, bestMove, name):
        """
        Method to report previous move to user
        """
        print("\n" + name + " places checker in column " + bestMove)
        
    def getIntAnswer(self, question):
        """
        Method to ask a user a question and check whether the input is a valid integer
        """
        answer = 0
        valid = False

        # Ask for a number
        print(question + " ") 
        while(not valid):
            try:
                x = input()
                answer = int(x)
                valid = True   # this must be a valid input
            except ValueError:
                self.reportToUser("That was not a valid integer ")
                valid = False
                print(question + " ")   
        return answer

    def reportToUser(self, message):
        """
        Method to report something to the user
        """
        print(message)
        
    def getAnswer(self, message):
        """
        Method that asks the inputted question and returns the answer
        """
        print(message)
        return input()

