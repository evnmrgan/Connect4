
# coding: utf-8

# In[ ]:


# A class which holds a move and a value.  Allows two values to be returned
# at once.
class Connect4Move:
    def __init__(val, mov):
        self.value = val
        self.move = mov

