# John Zelesny
# CS 110 Final Project

# This creates the object for the Entrance room
# 1's mean Yes, 0's mean no

class EntranceRoom:

    # Initilizes the door and key in the room
    def __init__(self):
        self.__keyTable = 1
        self.__lockedDoor = 1

    # Changes the key to No (player pick up the key)
    def takeKey(self):
        self.__keyTable = 0
    
    # Changes the door to No (player opens the door)
    def openDoor(self):
        self.__lockedDoor = 0

    # Returns if key is taken
    # Returns True if not taken
    # Returns False if taken
    def keyExists(self):
        return self.__keyTable == 1

    def reset(self):
        self.__keyTable = 1
        self.__lockedDoor = 1
    # Returns if door is unlocked
    # Returns True if locked
    # Returns False if unlocked
    def doorLocked(self):
        return self.__lockedDoor == 1

    def __str__(self):
        return "Key: " + str(self.__keyTable) + "\n"\
               "Door: " + str(self.__lockedDoor)


##test = EntranceRoom()
##print(test.__str__())
##test.takeKey()
##print(test.__str__())
##test.openDoor()
##print(test.__str__())
