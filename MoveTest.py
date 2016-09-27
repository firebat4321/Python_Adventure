class Movement:

  def __init__(self):
    self.__localList = ['Entrance','Lobby','Kitchen','Cave','Lab','Final','End']
    self.__location = self.__localList[0]

  def changeLocation(self,number):
    self.__location = self.__localList[number]
  def reset(self):
    self.__location = self.__localList[0]

  def returnLocation(self):
    return self.__location

##moveTest = Movement()
##print(moveTest.returnLocation())
##moveTest.changeLocation(1)
##print(moveTest.returnLocation())
##moveTest.changeLocation(2)
