# John Zelesny
# CS 110 Final Project

# This creates the object for the Lobby
# 1's means Yes, 0's mean No, -1 means Does not exist

class LobbyRoom:

    # Initilizes the gold under the couches and the locked door
    def __init__(self):
        self.__gold = 1
        self.__lockedDoor = 1

    # Changes the gold to No (player takes the gold)
    def takeGold(self):
        self.__gold = 0
        
    def openDoor(self):
        self.__lockedDoor=0

    def closeDoor(self):
        self.__lockedDoor = 1

    def destroyDoor(self):
        self.__lockedDoor = -1

    def lockedDoor(self):
        return self.__lockedDoor == 1

    def openedDoor(self):
        return self.__lockedDoor == 0


    def noDoor(self):
        return self.__lockedDoor == -1
    # Returns if gold is taken
    # Returns True if not
    # Returns False if taken
    def goldExists(self):
        return self.__gold == 1
    def reset(self):
        self.__gold = 1
        self.__lockedDoor = 1

    def __str__(self):
        return "Gold: " + str(self.__gold)

##test = LobbyRoom()
##print(test.goldExists())
##test.takeGold()
##print(test.goldExists())
