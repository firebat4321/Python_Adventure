##Matthew Lee & John Zelesny
##CS 110 Final Project

##Analysis
##Create a GUI to use the main.py
##It will display the description of the room in the top frame.
##It will display an entry box so the user can input commands in the middle.
##It will display 'quit', 'submit', and 'commands' buttons on the bottom, and the score above that.


#design:
#import program and tkinter
from tkinter import *
#module
import mainGUI
#create GUI
##mainGUI.main()
##import objects
import EntranceRoom
import LobbyRoom
import Score
import MoveTest
import KitchenRoom
import Cave
import Lab
import FinalRoom

entranceObject = EntranceRoom.EntranceRoom()
lobbyObject = LobbyRoom.LobbyRoom()
kitchenObject = KitchenRoom.KitchenRoom()
scoreObject = Score.Score()
moveObject = MoveTest.Movement()
caveObject =Cave.Cave()
labObject=Lab.Lab()
finalObject=FinalRoom.Final()

class textGUI:
  #initiate window and widgets
  def __init__(self):
    self.root=Tk()
##create frames for buttons,
    self.topFrame=Frame(self.root)
    self.middleFrame=Frame(self.root)
    self.bottomFrame=Frame(self.root)

##create stringVars and Labels to display various text
    self.descriptionVar=StringVar()
    self.scoreVar=StringVar()
    self.actionDescriptionVar=StringVar()
    self.placeVar=StringVar()

    
    self.descriptionLabel=Label(self.topFrame, textvariable=self.descriptionVar)
    self.scoreLabel=Label(self.middleFrame, textvariable=self.scoreVar)
    self.actionDescriptionLabel=Label(self.middleFrame, textvariable=self.actionDescriptionVar)
    self.placeLabel=Label(self.topFrame, textvariable=self.placeVar)
##set stringVars

    self.actionDescriptionVar.set("The last thing you remeber is falling into a pit.\n"
                                  "But as you come to your senses, you realize you're in another room!")
    self.placeVar.set(mainGUI.getPlace())
    self.descriptionVar.set(mainGUI.entranceDescription())
    self.scoreVar.set(0)


##Label for the 'score'
    self.wordScoreLabel=Label(self.middleFrame, text='Score')
    

##Create Label for action Entry
    self.actionLabel=Label(self.middleFrame, text="Enter Action:")
    
##create entry for action
    self.actionEntry=Entry(self.middleFrame, width=20)

##create  quit submit and commands buttons.
    self.quitButton=Button(self.bottomFrame, text="Quit", command=self.root.destroy)
    self.submitButton=Button(self.bottomFrame,text="Submit", command=self.submitCommand)
    self.commandsButton=Button(self.bottomFrame,text="HELP", command=self.displayCommands)
    self.restartButton=Button(self.bottomFrame, text ="Restart", command = self.restart)
##Pack everything
    self.topFrame.pack()
    self.middleFrame.pack()
    self.bottomFrame.pack()
##Top frame things
    self.placeLabel.pack()
    self.descriptionLabel.pack()
##MiddleFrame
    self.actionLabel.pack()
    self.actionEntry.pack()
    self.actionDescriptionLabel.pack()
    self.wordScoreLabel.pack()
    self.scoreLabel.pack()
##Bottom Frame
    self.submitButton.pack(side='left')
    self.commandsButton.pack(side='left')
    self.restartButton.pack(side='left')
    self.quitButton.pack(side='left')
    

#Binded Entry
    self.actionEntry.bind('<Return>', self.submitCommandBind)


    mainloop()

    #send text into text in main, then get the result back, display it.
  def submitCommand(self):
    text=self.actionEntry.get()
    textGet=mainGUI.action(text)
    self.actionDescriptionVar.set(textGet)
    room=mainGUI.getPlace()
    self.placeVar.set(room)
    description=mainGUI.placeDescription()
    self.descriptionVar.set(description)
    score=mainGUI.getScore()
    self.scoreVar.set(score)
    self.actionEntry.delete(0, END)
    #message box for 'commands'

  def submitCommandBind(self,event):
    text=self.actionEntry.get()
    textGet=mainGUI.action(text)
    self.actionDescriptionVar.set(textGet)
    room=mainGUI.getPlace()
    self.placeVar.set(room)
    description=mainGUI.placeDescription()
    self.descriptionVar.set(description)
    score=mainGUI.getScore()
    self.scoreVar.set(score)
    self.actionEntry.delete(0, END)

  def restart(self):
    entranceObject.reset()
    lobbyObject.reset()
    kitchenObject.reset()
    scoreObject.reset()
    moveObject.reset()
    caveObject.reset()
    labObject.reset()
    finalObject.reset()
    mainGUI.entranceObject.reset()
    mainGUI.lobbyObject.reset()
    mainGUI.kitchenObject.reset()
    mainGUI.scoreObject.reset()
    mainGUI.moveObject.reset()
    mainGUI.caveObject.reset()
    mainGUI.labObject.reset()
    mainGUI.finalObject.reset()
    self.actionDescriptionVar.set("The last thing you remeber is falling into a pit.\n"
                                  "But as you come to your senses, you realize you're in another room!")
    room=mainGUI.getPlace()
    self.placeVar.set(room)
    description=mainGUI.placeDescription()
    self.descriptionVar.set(description)
    score=mainGUI.getScore()
    self.scoreVar.set(score)
    self.actionEntry.delete(0, END)
  def displayCommands(self):
    messagebox.showinfo("HELP",\
                        "To interact with the text Adventure, You type:"
                        "<command><space><object>\n"\
                        "For example, \n"
                        "Move East\n"
                        "\n"
                        "Objects are capitalized, and these here is the list of commands:\n\n"
                        "MOVE USE TAKE LOOK HELP\n"
                        "If you pick up an item in a room,\n"
                        "You may be able to use it in a different room."
                        "EX: Use knife")


def main():

  GUI=textGUI()
main()

