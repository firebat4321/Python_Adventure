# John Zelesny
# CS 110 Final Project

# This creates an object to keep score
# Function is called to add one to score each time
# Function displays total score at the end

class Score:

    # Intitilizes score to 0
    def __init__(self):
        self.__score = 0

    # Adds one to score each time it's called
    def addOne(self):
        self.__score += 1
    def reset(self):
        self.__score=0

    # Returns total score
    def displayScore(self):
        return self.__score

##test = Score()
##print(test.displayScore())
##test.addOne()
##print(test.displayScore())
