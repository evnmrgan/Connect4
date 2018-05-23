
# coding: utf-8

# In[ ]:


# Holds information about and interacts with a human player

class HumanConnect4Player(Player):

    def __init__(self, name):
        super().__init__(name)
        
    def getMove(self, state, view):
        """
        Gets a move for the user
        """
        return view.getUserMove(state)

