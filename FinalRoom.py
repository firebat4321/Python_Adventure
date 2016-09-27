# John Zelesny, Matt Lee
# CS 110 Final Project

# Creates the object for the Final room
# 1's mean Yes, 0's mean no

class Final:
  def __init__(self):
    self.__monsterSeen = 0

  def monsterExist(self):
    return self.__monsterSeen

  def monsterNotice(self):
    self.__monsterSeen = 1

  def reset(self):
    self.__monsterSeen = 0
