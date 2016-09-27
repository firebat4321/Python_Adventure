##Mattthew Lee
##CS110 Final Project
##
##This creates the room (object) for the cave.
##1's mean yes, 0's mean no.

class Cave:
  def __init__(self):
    self.__bear=1
    self.__water=1

  def takeWater(self):
    self.__water=0

  def killBear(self):
    self.__bear=0

  def reset(self):
    self.__bear=1
    self.__water=1
  
  def bearExists(self):
    return self.__bear==1

  def waterExists(self):
    return self.__water==1

  def __str__(self):
    return "Water: " +str(self.__water)\
           +"Bear: " +str(self.__bear)
  
  
