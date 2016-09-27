#Matthew Lee
##CS 110 Final Project

##This creates the object for the Kitchen
##1's mean Yes, 0's mean no

class KitchenRoom:

##  Initialize the existing items in the room
  def __init__(self):
    self.__knife=1
    self.__honey=1
    self.__meat=1
    self.__axe=1

##Items go away if they take the item
  def takeKnife(self):
    self.__knife=0

  def takeHoney(self):
    self.__honey=0

  def takeMeat(self):
    self.__meat=0

  def takeAxe(self):
    self.__axe=0

##Check to see if the items are still in the room.
  def knifeExists(self):
    return self.__knife ==1
  def honeyExists(self):
    return self.__honey ==1
  def meatExists(self):
    return self.__meat ==1
  def axeExists(self):
    return self.__axe==1

  def reset(self):
    self.__knife=1
    self.__honey=1
    self.__meat=1
    self.__axe=1
  def __str__(self):
    return "Knife: " + str(self.__knife)\
           + "Honey: " + str(self.__honey)\
           + "Meat: " + str(self.__meat)
