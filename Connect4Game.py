
# coding: utf-8

# In[ ]:


# Represents the state of the Connect4 game. It is the model in the model-view-controller pattern.

class Connect4Game:
    playerToMoveNum = None    # 0 or 1 for first and second player
    board = None  # 2D array to represent the board
    players = [None, None]  # Array of the two players

    # Initialize helper function goes here, once computer player is implemented

    def __init__(self, playerNum, thePlayers):
        initBoard = [[] for row in range(ROWS)]
        # loop through 2D array elements and place EMPTY character
        for i in range(0, ROWS):
            for j in range(0, COLS):
                initBoard[i].append(EMPTY)
        
        # construct a board
        self.board = [[] for row in range(ROWS)]
        for i in range(0, ROWS):
            for j in range(0, COLS):
                self.board[i].append(initBoard[i][j])          

        self.playerToMoveNum = playerNum
        self.players = thePlayers


    def getBoard(self):
        """
        Getter method for the 2D array of the board. The first [] index represents rows
        The second [] index represents columns
        """
        return self.board

    def getPlayers(self):
        """
        Getter method for the array holding Player objects
        """
        return self.players

    def getPlayerNum(self):
        """
        Getter method for the number of the player whose turn it is
        """
        return self.playerToMoveNum

    def getPlayerToMove(self):
        """
        Getter method for the player to move
        """
        return self.players[self.getPlayerNum()]
 
    def isValidMove(self, col): 
        """
        Method to check whether an inputted column number is a valid move
        """
        if((col >= 0 and col < COLS) and (self.board[ROWS - 1][col] == EMPTY)):
            return True
        else:
            print("Not a valid move")
            return False
        
    def makeMove(self, col): 
        """
        Method that places a checker in the right position according to gravity
        and empty spots
        """
        currChecker = CHECKERS[self.playerToMoveNum] # uses the current player number to determine the correct piece
        if(self.isValidMove(col)): # confirm the column is available
            for row in range(0, ROWS): # loop through each row in the column
                if(self.board[row][col] == EMPTY): # add the checker if the space is empty
                    self.board[row][col] = currChecker 
                    self.playerToMoveNum = 1 - self.playerToMoveNum   # Switch player 
                    break

    def isFull(self):
        """
        Method to check whether the entire board is full
        """
        for col in range(0, COLS):
            if(self.board[ROWS - 1][col] == EMPTY):
                return False
        return True

    # 

    def isWinner(self):
        """
        Method to loop through the board horizontally, vertically, diagonally from bottom left to top right
        and diagonally from top left to bottom right, and check for four checkers in a row
        loop through each element in the board and check for matching checkers horizontally
        """
        currChecker = CHECKERS[1 - self.playerToMoveNum] # uses the current player number to determine the correct piece
        
        for r in range(0, ROWS):
            count = 0
            for c in range(0, COLS):
                if(self.board[r][c] == currChecker): # if the character matches add to the count
                    count+=1
                    if (count == 4):
                        return True # return true when the count hits 4 in a row
                else: # reset the counting, potential sequence has been interrupted
                    count = 0

        # loop through each element in the board and check for matching checkers vertically
        for c in range(0, COLS):
            count = 0;
            for r in range(0, ROWS):
                if(self.board[r][c] == currChecker): # if the character matches add to the count
                    count+=1
                    if(count == 4):
                        return True
                else: # reset the counting, potential sequence has been interrupted
                    count = 0

    # loop through possible elements in the board and check for matching checkers diagonally from bottom left to top right
        for c in range(0, COLS):
            for r in range(0, ROWS):
                count = 0
                for delta in range(0, 4): # extra for loop to check elements diagonally
                    if (((r + delta) >= ROWS or ((c + delta)) >= COLS)):
                        #print("out of bounds at row " + str(r + delta) + ", column " + str(c + delta))
                        count = 0 # break the count if it's out of bounds
                        break
                    elif(self.board[r + delta][c + delta] == currChecker): # if the character matches add to the count
                        #print("match in row " + str(r + delta) + ", column " + str(c + delta))
                        count+=1
                        if(count == 4):
                            return True
                    else:
                        #print("no match at row " + str(r + delta) + ", column " + str(c + delta))
                        count = 0
                        break
            
    # loop through possible elements in the board and check for matching checkers diagonally from top left to bottom left
        for c in range(0, COLS):
            for r in range(0, ROWS):
                count = 0
                for delta in range(-3, 1): # extra for loop to check elements diagonally
                    if(((r + delta) < 0 or ((c - delta)) >= COLS)):
                        count = 0    # break the count if it's out of bounds
                        break
                    elif(self.board[r + delta][c - delta] == currChecker): # if the character matches add to the count
                        count+=1
                        if(count == 4):
                            return True
                    else:
                        count = 0
                        break
        return False # if all for loops have finished, there are no winners
 
    def gameIsOver(self):
        """
        Method to determine whether the game has ended, checks if board is full or if there's a winner
        """
        return self.isFull() or self.isWinner()

    def staticEvaluator(self):
        """
        Static evaluator to determine the value of a specific board move/setup
        """
        total = 0 # variable to store the total value of a board setup
        value = 0 # variable to store the temporary value of a potential 4-in-a-row
        
        otherChecker = CHECKERS[self.playerToMoveNum] # the checker we don't want to find
        currChecker = CHECKERS[1 - self.playerToMoveNum] # the checker we want to find
        
        # check the board horizontally, loop through potential 4-in-a-rows and 
        # count how many matching checkers there are with the player whose turn it is
        # if there is one of the other player's checkers, the 4-in-a-row is invalid
        # print("Evaluating for: " + currChecker)
        for row in range (0, ROWS):
            for col in range(0,COLS):
                value = 0
                for next in range(0,4):
                    if(col + next >= COLS):
                        break
                    if (self.board[row][col + next] != currChecker):
                        break
                    else:
                        value+=1
                if (value > 0):
                    total += (value**2) # if value is positive, add weighted value to total
                    #print("Adding to total from horizontal at (" + str(row) + ", " + str(col) + "): " + str(value**2))

        
        # check the board vertically, loop through potential 4-in-a-rows and 
        # count how many matching checkers there are with the player whose turn it is
        # if there is one of the other player's checkers, the 4-in-a-row is invalid
        for col in range(0,COLS):
            for row in range(0,ROWS):
                value = 0
                for next in range(0,4):
                    if(row + next >= ROWS):
                        break
                    if (self.board[row + next][col] != currChecker):
                        break
                    else:
                        value+=1
                if (value > 0):
                    total += (value**2) # if value is positive, add weighted value to total
                    #print("Adding to total from vertical at (" + str(row) + ", " + str(col) + "): " + str(value**2))
        
        # check the board diagonally from bottom left to top right, loop through potential 4-in-a-rows and 
        # count how many matching checkers there are with the player whose turn it is
        #if there is one of the other player's checkers, the 4-in-a-row is invalid
        for col in range(0,COLS-3):
            for row in range(0,ROWS-3):
                value = 0
                for next in range(0,4):
                    if ((row + next) >= ROWS or (col + next) >= COLS):
                        break
                    elif (self.board[row + next][col + next] != currChecker):
                        break
                    else:
                        value+=1
                    if (value > 0):
                        total += (value**2) # if value is positive, add weighted value to total
                        #print("Adding to total from up diagonal at (" + str(row) + ", " + str(col) + "): " + str(value**2))
                
        #check the board diagonally from top left to bottom right, loop through potential 4-in-a-rows and 
        #count how many matching checkers there are with the player whose turn it is
        #if there is one of the other player's checkers, the 4-in-a-row is invalid
        for col in range(0,COLS-3):
            for row in range(ROWS-3, ROWS):
                value = 0
                for next in range(0,4):
                    if ((row - next) < 0 or ((col + next)) >= COLS):
                        break
                    elif (self.board[row - next][col + next] != currChecker):
                        break
                    else:
                        value+=1
                    if (value > 0):
                        total += (value**2) # if value is positive, add weighted value to total
                        #print("Adding to total from down diagonal at (" + str(row) + ", " + str(col) + "): " + str(value**2))
        return total

