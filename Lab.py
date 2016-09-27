##Mattthew Lee
##CS110 Final Project
##
##This creates the room (object) for the cave.
##1's mean yes/on, 0's mean no/off.

##Initialize self
class Lab:
  def __init__(self):
    self.__paper=0
    self.__computer=1
  def createPaper(self):
    self.__paper=1

  def takePaper(self):
    self.__paper=2

  def shutDown(self):
    self.__computer=0

  def paperExists(self):
    return self.__paper == 1
  def paperGot(self):
    return self.__paper == 2
  def computerOn(self):
    return self.__computer==1

  def reset(self):
    self.__paper=0
    self.__computer=1

  def __str__(self):
    return "Computer: "+ str(self.__computer)\
           +"Paper: " + str(self.__paper)
