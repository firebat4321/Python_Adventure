# John Zelesny & Matthew Lee
# CS 110 Final Project

#The text will be sent and
#this will return information (description, ' information, and score.)

INVALID="Invalid Command."
INPUT="Input a command: "
HELP="Commands: Look, Use, Take, Move"
# Import Room Classes
import EntranceRoom
import LobbyRoom
import Score
import MoveTest
import KitchenRoom
import Cave
import Lab
import FinalRoom
# Create Room Objects in main()"
entranceObject = EntranceRoom.EntranceRoom()
lobbyObject = LobbyRoom.LobbyRoom()
kitchenObject = KitchenRoom.KitchenRoom()
scoreObject = Score.Score()
moveObject = MoveTest.Movement()
caveObject =Cave.Cave()
labObject=Lab.Lab()
finalObject=FinalRoom.Final()

#Define functions to send and return information.
def getPlace():
  return moveObject.returnLocation()  


# Define description functions
def entranceDescription():
  if entranceObject.keyExists():
    return ("The room is made of brick walls, two torches giving light.\n"\
            "A barred DOOR to the EAST blocks the only way out, showing a lavish room on the other side.\n"\
            "A table sits in the middle of the room.\n"
            "There is a SIGN on the door.\n"
            "A golden KEY sits alone on the table.")
  else:
    return ("The room is made of brick walls, two torches giving light.\n"\
            "A barred DOOR to the EAST blocks the only way out, showing a lavish room on the other side.\n"\
            "A table sits in the middle of the room.\n"
            "There is a SIGN on the door.\n"
            "The table stands bare.")
##  
##  if entranceObject.keyExists():
##    print("A golden KEY sits alone on the table.")
##  else:
##    print("The table stands bare.")
##  print("The room is made of brick walls, two torches giving light.\n"\
##        "A barred DOOR to the EAST blocks the only way out, showing a lavish room on the other side.\n"\
##        "A table sits in the middle of the room.\n"
##        "There is a SIGN on the door.")
##  if entranceObject.keyExists():
##    print("A golden KEY sits alone on the table.")
##  else:
##    print("The table stands bare.")

def lobbyDescription():
  if not lobbyObject.goldExists() and lobbyObject.lockedDoor():
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "Two double DOORS to the NORTH are closed, barred with wood.\n"
            "The barred door to the Entrance is still open to the WEST."
            "All the cushions from the couches litter the floor")
  elif lobbyObject.goldExists() and lobbyObject.lockedDoor():
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "Two double DOORS to the NORTH are closed, barred with wood.\n"
            "The barred door to the Entrance is still open to the WEST.")
  elif not lobbyObject.goldExists() and lobbyObject.openedDoor():
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "Two double DOORS to the NORTH are opened.\n"
            "The barred door to the Entrance is still open to the WEST."
            "All the cushions from the couches litter the floor")

  elif lobbyObject.goldExists() and lobbyObject.openedDoor():
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "Two double DOORS to the NORTH are opened.\n"
            "The barred door to the Entrance is still open to the WEST.")
  elif not lobbyObject.goldExists() and lobbyObject.noDoor():
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "The DOORS are destroyed, and the entrance NORTH is open.\n"
            "The barred door to the Entrance is still open to the WEST."
            "All the cushions from the couches litter the floor")
  else:
    return ("The room is decorated in lavish white walls and gold trim.\n"
            "A large CHANDELIER up above gives the room light.\n"
            "Red velvet COUCHES line the walls, paintings just above them.\n"
            "A door to the EAST opens up into a large kitchen.\n"
            "The DOORS are destroyed, and the entrance NORTH is open.\n"
            "The barred door to the Entrance is still open to the WEST.")
    
##  print("The room is decorated in lavish white walls and gold trim.\n"
##        "A large CHANDELIER up above gives the room light.\n"
##        "Red velvet COUCHES line the walls, paintings just above them.\n"
##        "A door to the EAST opens up into a large kitchen.\n"
##        "Two double DOORS to the NORTH are closed, barred with wood.\n"
##        "The barred door to the Entrance is still open to the WEST.")
##  if not lobbyObject.goldExists():
##    print("\nAll the cushions from the couches litter the floor")

def kitchenDescription():
  if kitchenObject.meatExists():
    return ("Something smells good.\n"
            "The walls, floor, and ceiling is covered in a black and white square pattern.\n"
            "On one side you see a typical kitchen setup.\n"
            "There is a COUNTER, a STOVE, a FAN, LIGHTS, and CUPBOARDS.\n"
            "In the middle of the room, there is a TABLE.\n"
            "The room feels slightly humid.\n"
            "An entrance is open to the WEST")
  else:
    return ("The walls, floor, and ceiling is covered in a black and white square pattern.\n"
            "On one side you see a typical kitchen setup.\n"
            "There is a COUNTER, a STOVE, a FAN, LIGHTS, and CUPBOARDS.\n"
            "In the middle of the room, there is a TABLE.\n"
            "The room feels slightly humid.\n"
            "An entrance is open to the WEST")
##  if kitchenObject.meatExists():
##    print("\nSomething smells good.")

##  print("The walls, floor, and ceiling is covered in a black and white square pattern.\n"
##        "On one side you see a typical kitchen setup.\n"
##        "There is a COUNTER, a STOVE, a FAN, LIGHTS, and CUPBOARDS.\n"
##        "In the middle of the room, there is a TABLE.\n"
##        "The room feels slightly humid.")
##  if kitchenObject.meatExists():
##    print("\nSomething smells good.")
    
def caveDescription():
  if (caveObject.waterExists() and caveObject.bearExists()):
    return ("It seems very wet, this must be where the moisture is coming from.\n"
            "You see water dripping from the ceiling of the cave.\n"
            "You see another entrance to the NORTH, but you cannot see where it leads too.\n"
            "The doorway SOUTH is still open.\n"
            "There is a puddle of WATER in front of you.\n"
            "Unfortunately, there is a BEAR in a red-tethered shirt at the end in your way.\n"
            "Next to the bear, you see many corpses.\n"
            "Fortunately, it doesn't seem to be hostile (yet).\n"
            "There is also a hole between you and the BEAR.\n"
            "There is a deep hole.")
  elif caveObject.waterExists():
    return ("It seems very wet, this must be where the moisture is coming from.\n"
            "You see water dripping from the ceiling of the cave.\n"
            "You see another entrance to the NORTH, but you cannot see where it leads too.\n"
            "The doorway behind you is still open.\n"
            "There is a puddle of WATER in front of you.\n"
            "There is a deep hole.")
  elif caveObject.bearExists():
    return ("It seems very wet, this must be where the moisture is coming from.\n"
            "You see water dripping from the ceiling of the cave.\n"
            "You see another entrance to the NORTH, but you cannot see where it leads too.\n"
            "The doorway behind you is still open.\n"
            "Unfortunately, there is a BEAR in a red-tethered shirt at the end in your way.\n"
            "Next to the bear, you see many corpses.\n"
            "Fortunately, it doesn't seem to be hostile (yet).\n"
            "There is also a hole between you and the BEAR.\n"
            "There is a deep hole.")
  else:
    return ("It seems very wet, this must be where the moisture is coming from.\n"
            "You see water dripping from the ceiling of the cave.\n"
            "You see another entrance to the NORTH, but you cannot see where it leads too.\n"
            "The doorway SOUTH is still open.\n"
            "There is a deep hole.")


##  print("It seems very wet, this must be where the moisture is coming from.\n"
##        "You see water dripping from the ceiling of the cave.\n"
##        "You see another entrance to the NORTH, but you cannot see where it leads too.\n"
##        "The doorway behind you is still open.")
##  if caveObject.waterExists():
##    print("\nThere is a puddle of WATER in front of you.")
##  if caveObject.bearExists():
##    print("Unfortunately, there is a BEAR in a red-tethered shirt at the end in your way.\n"
##          "Next to the bear, you see many corpses.\n"
##          "Fortunately, it doesn't seem to be hostile (yet).\n"
##          "There is also a hole between you and the BEAR.")
##  else:
##    print("\nThere is a deep hole.")

def labDescription():
  if labObject.computerOn():
    return ("You enter an old looking bunker of sorts. Old databases with film line the walls.\n"
            "Many tables next to the databases have computers on top of them, their screens mashed and broken.\n"
            "While many of the tables are empty, one TABLE has torn papers all over it.\n"
            "There is also a staircase that goes UP."
            "But wait! One COMPUTER is on.\n"
            "The door SOUTH leads back to the cave.")
  else:
    return ("You enter an old looking bunker of sorts. Old databases with film line the walls.\n"
            "Many tables next to the databases have computers on top of them, their screens mashed and broken.\n"
            "While many of the tables are empty, one TABLE has torn papers all over it.\n"
            "There is also a staircase that goes UP.\n"
            "The door SOUTH leads back to the cave.")
##  print("You enter an old looking bunker of sorts. Old databases with film line the walls.\n"
##        "Many tables next to the databases have computers on top of them, their screens mashed and broken.\n"
##        "While many of the tables are empty, one TABLE has torn papers all over it.\n"
##        "There is also a staircase that goes UP.")
##  if labObject.computerOn():
##    print("\nBut wait! One COMPUTER is on.")

def finalDescription():
  if not finalObject.monsterExist():
    finalObject.monsterNotice()
    return ("As you walk out of the trap door in the Labs, you're blinded by a bright light.\n"
            "As you squint, you realise the light it coming from the sun! You made it outside!\n"
            "But as you step out onto the grass, you hear the earth rumble.\n"
            "When suddenly, from the trees, comes a giant green monster wielding a giant decorated tree!\n"
            "'Cower in fear, little mortal, for I am the dreaded TOKENIZER!!' the monster proclaims!\n"
            "'I shall crush you under my parse tree as punishment for entering my domain!'\n"
            "You can still retreat back DOWN.")
  else:
    return ("As you walk out of the trap door in the Labs, you're blinded by a bright light.\n"
            "As you squint, you realise the light it coming from the sun! You made it outside!\n"
            "The TOKENIZER is still about, slamming its parse tree against the ground as it spots you.\n"
            "'Come back for more, eh?!' it shouts down at you and raises it's tree.\n"
            "You can still retreat back DOWN.")
##  print("As you walk out of the trap door in the Labs, you're blinded by a bright light.\n"
##        "As you squint, you realise the light it coming from the sun! You made it outside!\n")
##  if not finalObject.monsterExist():
##    print("But as you step out onto the grass, you hear the earth rumble.\n"
##          "When suddenly, from the trees, comes a giant green monster wielding a giant decorated tree!\n"
##          "'Cower in fear, little mortal, for I am the dreaded TOKENIZER!!' the monster proclaims!\n"
##          "'I shall crush you under my parse tree as punishment for entering my domain!'")
##    finalObject.monsterNotice()
##  else:
##    print("The TOKENIZER is still about, slamming its parse tree against the ground as it spots you.\n"
##          "'Come back for more, eh?!' it shouts down at you and raises it's tree.")
  
# Opening prompt
##print("The last thing you remeber is falling into a pit.\n"
##      "But as you come to your senses, you realize you're in another room!")

# Main movement hub. Returns each time and checks location.
# As location updates, different functions are called.
def main():
  entranceObject = EntranceRoom.EntranceRoom()
  lobbyObject = LobbyRoom.LobbyRoom()
  kitchenObject = KitchenRoom.KitchenRoom()
  scoreObject = Score.Score()
  moveObject = MoveTest.Movement()
  caveObject =Cave.Cave()
  labObject=Lab.Lab()
  finalObject=FinalRoom.Final()
def action(entry):
  if moveObject.returnLocation() == 'Entrance':
    textReturn =entrance(entry)
    return textReturn
  elif moveObject.returnLocation() == 'Lobby':
    textReturn =lobby(entry)
    return textReturn
  elif moveObject.returnLocation() == 'Kitchen':
    textReturn =kitchen(entry)
    return textReturn
  elif moveObject.returnLocation() == 'Cave':
    textReturn =cave(entry)
    return textReturn
  elif moveObject.returnLocation() == 'Lab':
    textReturn =lab(entry)
    return textReturn
  elif moveObject.returnLocation() == 'Final':
    textReturn =final(entry)
    return textReturn
  else:
    return "The End!"

def placeDescription():
  if moveObject.returnLocation() == 'Entrance':
    return entranceDescription()
  elif moveObject.returnLocation() == 'Lobby':
    return lobbyDescription()
  elif moveObject.returnLocation() == 'Kitchen':
    return kitchenDescription()
  elif moveObject.returnLocation() == 'Cave':
    return caveDescription()
  elif moveObject.returnLocation() == 'Lab':
    return labDescription()
  elif moveObject.returnLocation() == 'Final':
    return finalDescription()
  else:
    return ""

def getScore():
  return scoreObject.displayScore()


##    else:
##      print("Game over.\n"
##        "Total score: " + str(scoreObject.displayScore()))
##  print("Game over.\n"
##        "Total score: " + str(scoreObject.displayScore()))
  
def entrance(entry):
##  entranceDescription()
  text = entry
  text=text.upper()
  if text == 'TAKE KEY':
    if entranceObject.keyExists():
      entranceObject.takeKey()
      scoreObject.addOne()
      return ("You pick up the key and pocket it")
    else:
      return ("You already have the key in your pocket")
  elif text == ('LOOK SIGN' or 'USE SIGN'):
    return ("Abandon hope all ye who enter here.")
  elif text == 'TAKE SIGN':
    return ("The sign is stuck to the door.\n"
            "You try to take it off, but your fingers get tired and you stop.")
  elif (text == 'USE DOOR'):
    if entranceObject.keyExists():
      return ("The door is locked shut.")
    else:
      if entranceObject.doorLocked():
        entranceObject.openDoor()
        scoreObject.addOne()
        return ("You use the key, and the door opens with a click")
      else:
        return ("The door is already opened!")
  elif (text == 'USE KEY'):
    if entranceObject.keyExists():
      return ("Key? What Key? You have no key.")
    else:
      if entranceObject.doorLocked():
        entranceObject.openDoor()
        scoreObject.addOne()
        return ("You use the key, and the door opens with a click")
      else:
        return ("The door is already opened!")
  elif text == 'LOOK DOOR':
      return ("The door is made of soild steel.\n"
              "You doubt even your monster strength could bend those bars.")
  elif text == 'LOOK KEY':
      return ("Just a normal, golden colored key.\n"
              "Maybe it opens some sort of door?")
  elif text == 'LOOK ROOM':
      return entranceDescription()
  elif text == 'LOOK EAST':
      return ("You see behind the bars, a lobby filled with a chandelier, \
couches, and you're able to see another room.")
  elif text == 'MOVE EAST':
      if entranceObject.doorLocked():
        return ("The door is locked tight still.")
      else:
        moveObject.changeLocation(1)
        return ("You move past the doors and into the lavish room.")
  elif text == 'HELP':
    return (HELP)
  else:
    return (INVALID)

def lobby(entry):
##  lobbyDecription()
  text = entry
  text=text.upper()
  if text == 'LOOK CHANDELIER': 
    return ("Its a large mass of glittering dimonds just over here.\n"
          "The light being reflected though the dimonds give the whole room light")
  elif text == 'USE CHANDELIER':
    return ("You start to jump at the chandelier, trying to grab for its many dimonds.\n"
          "But its too far out of reach. Curses for being born so short!!")
  elif text == 'USE DOORS':
    if lobbyObject.lockedDoor():
      lobbyObject.openDoor()
      return ("You unbar the doors, and they open up.")
    elif lobbyObject.openedDoor():
      lobbyObject.closeDoor()
      return ("You close the doors and bar them.")
      
    else:
      return ("The door is broken, you can't use this.")
  elif text =="LOOK DOORS":
    if lobbyObject.lockedDoor():
      return ("These are just normal doors, locked with a piece of wood inserted between the two handles so it doesn't open.")
    elif lobbyObject.openedDoor():
      return ("The piece of wood is set aside, and the doorway is open.  Through the doorway you see a cave.")
    else:
      return ("You look at the shattered wood on the ground.  Good thing you're wearing boots.")
    
  elif text == "USE AXE":
    if (not kitchenObject.axeExists() and (lobbyObject.openedDoor() or lobbyObject.lockedDoor())):
      scoreObject.addOne()
      lobbyObject.destroyDoor()
      return ("You destructively strike the doors down, and it shatters into a thousand pieces.")

    else:
      return (INVALID)
  elif text =="LOOK EAST":
    return ("You see the only way out.")
  elif text == 'LOOK COUCHES':
    if lobbyObject.goldExists():
      return ("You look over at the plush couches. They look very comfy!\n"
              "However, you see some lumps pressing out from under the CUSHIONS.")
    else:
      return ("The cushion-less couches look a little less comfy now.")
  elif text == 'USE COUCHES':
    if lobbyObject.goldExists():
      return ("You take a seat on the plush couch. It IS rather comfy!\n"
            "Except for those little lumps under the CUSHIONS...")
    else:
      return ("You sit on the cushion-less couch. It IS less comfy...")
  elif (text == 'USE CUSHIONS' or text== 'LOOK CUSHIONS'):
    if lobbyObject.goldExists():
      lobbyObject.takeGold()
      scoreObject.addOne()
      return ("You pick up one of the cushions from the couch and toss it aside.\n"
              "Under it, you find a wealth of odd objects: rocks, pennies, remotes, TV Guides.\n"
              "As you keep pulling up more cushions- Hey! Is that gold?\n"
              "You find some lost gold under the cushions! You think falling down that hole was a good idea!\n"
              "You pocket your new found wealth.")
    else:
      return ("You don't find anything else worth while under the cushions.")
  elif text == 'LOOK ROOM':
    return lobbyDecription()
  elif text == 'MOVE WEST':
    moveObject.changeLocation(0)
    return ("You walk through the barred doors back where you started.")
  elif text == "LOOK EAST":
    return ("Is.... that... a kitchen?!")
  elif text == 'MOVE EAST':
    moveObject.changeLocation(2)
    return ("You walk through the open door, and you enter a kitchen.")
  elif text == "LOOK WEST":
    return ("You see the room from whence you came!")
  elif text == 'MOVE NORTH':
    if lobbyObject.lockedDoor():
      return ("You are unable to go through, as the DOORS are closed with wood.")
    else:
      moveObject.changeLocation(3)
      return ("You move through the doorway, and you enter a cave.")
  elif text == "LOOK NORTH":
    return ("You see an entrance.")
  elif text == 'HELP':
    return (HELP)
  else:
    return (INVALID)

def kitchen(entry):
##  kitchenDescription()
  text=entry
  text=text.upper()
  if text == "LOOK COUNTER":
    if kitchenObject.knifeExists():
      return ("There is only a cutting board with some scraps of meat left over, and a KNIFE.")
    else:
      return ("There is only a cutting board with some scarps of meat left over.")
  elif text == "LOOK KNIFE":
    if kitchenObject.knifeExists():
      return ("The knife seems to be a very fine blade...")
    else:
      return ("The knife you took left a large dent in the cutting board. Unfortunately there are no more knives.")      
  elif text== "TAKE KNIFE":
    if kitchenObject.knifeExists():
      kitchenObject.takeKnife()
      return ("You put the knife in your pocket.")
    else:
      return ("There are no more knives.")
  elif text=="LOOK CUPBOARDS":
    if kitchenObject.honeyExists():
      return ("In one cupboard, on the left side is a jar of HONEY without a lid."
              "On the right side of each cupboard, you see various spices and seasoning.")
    else:
      return ("The left side of the cupboards are empty."
              "On the right side of each cupboard, you see various spices and seasoning.")
  elif text == "USE CUPBOARDS":
    return "Yes, put all your stuff in the cupboards, definitely a smart idea. NOT."
  elif text =="LOOK HONEY":
    if kitchenObject.honeyExists():
      return ("It's a jar of golden HONEY! looks yummy.")
    else:
      return ("It looks delicious.")
  elif text=="TAKE HONEY":
    if kitchenObject.honeyExists():
      scoreObject.addOne()
      kitchenObject.takeHoney()
      return ("You take the jar of honey and put it in your bag, hoping nothing spills.")
    else:
      return ("There is no honey!")
  elif text == "LOOK WEST":
    return ("You see the room with the COUCHES that you came from.")
  elif text == 'HELP':
    return (HELP)     
  elif text == "LOOK STOVE":
    return ("There is nothing in the stove, nor on the stove.")
  elif text == "USE STOVE":
    return ("The stove is not working")
  elif text == "LOOK FAN":
    return ("The fan is on, and seems to making the room less humid.")
  elif text == "USE FAN":
    return ("You try to turn the fan off, but the button doesn't seem to work. It's better on anyways.")
  elif text == "LOOK LIGHTS":
    return ("You look directly at the light.\nIt is so bright you're blinded for a few seconds.\n"
            "The light seems embedded in the wall, and there is nothing you can do about it.\n"
            "After looking away, you see the an AXE in a small corner of the room you didn't see before.")
  elif text == "USE LIGHTS":
    return ("You try to turn off the bright lights, or dim them, but you cannot find a button. You can't take it out because it's embedded in the wall.")
  elif text == "TAKE AXE":
    if kitchenObject.axeExists():
      scoreObject.addOne()
      kitchenObject.takeAxe()
      return ("You take the axe.")
    else:
      return ("You took the axe already.")
  elif text == "LOOK AXE":
    return ("You see a red axe with a wooden handle.")
  elif text == "LOOK TABLE":
    if kitchenObject.meatExists():
      return ("There is a plate of delicious meat on the table. Looks like venison. It also seems to be some fresh MEAT.")
    else:
      return ("The table has nothing on it.")
  elif text == "LOOK MEAT":
    return ("Mmmm. Looks tasty.")
  elif text =="TAKE MEAT":
    return ("It's too big to put in your pockets, and too awkward to carry.")
  elif text == "USE MEAT" or text == "USE KNIFE":
    if kitchenObject.meatExists() and not kitchenObject.knifeExists():
      kitchenObject.takeMeat()
      scoreObject.addOne()
      return ("You cut the meat into bite-size pieces."
              "Om nom nom. You eat the meat and you are full.")
    elif kitchenObject.meatExists():
      return ("You try to eat the meat, but it seems to be too big.")
    else:
      return ("There is no meat left in the kitchen.")
  elif text == "USE KNIFE":
    if kitchenObject.meatExists() and not kitchenObject.knifeExists():
      kitchenObject.takeMeat()
      scoreObject.addOne()
      return ("You cut the pieces into bite-size pieces."
              "OM NOM NOM. You eat the meat and you are full.")
    elif not kitchenObject.meatExists() and not kitchenObject.knifeExists():
      return ("Don't cut yourself.")
    else:
      return ("You're bored and knife the board.")
  elif text == "MOVE WEST":
    moveObject.changeLocation(1)
    return ("You move back to the Lobby.")
  else:
    return (INVALID)
  
def cave(entry):
  text=entry
  text=text.upper()
  if text == "MOVE NORTH":
    if caveObject.bearExists():
      moveObject.changeLocation(6)
      return ("You try to walk past the bear nonchalantly, but it doesn't work.\n"
              "As you walk past the bear, the bear attacks you and mauls you to death.")
    else:
      moveObject.changeLocation(4)
      return ("You move to the other end of the cave.\n"
              "You see another door, and open it.\n"
              "You enter a room...")
  elif text == "LOOK NORTH":
    return "It's too dark to see up ahead."
  elif text == 'HELP':
    return (HELP) 
  elif text == "MOVE SOUTH":
    moveObject.changeLocation(1)
    return ("You go back.")
  elif text == "LOOK SOUTH":
    return ("There's that room with the COUCHES again.")
  elif text == "USE BEAR":
    if caveObject.bearExists:
      moveObject.changeLocation(6)
      return ("You try talking to the bear, trying to convince it to let you pass.\n"
              "The bear talks back!\n"
              "You say: \"Hey bear, wanna let me through? There is some fresh meat in the house behind me.\"\n"
              "The bear responds: \"YOU'RE FRESH MEAT!\"\n"
              "The bear chases you down. You run, but the bear attempts to tackle you and you try to dodge, but the bear is just too fast.\n"
              "The bear tackles you down to the ground.\n"
              "The bear then proceeds to maul your face off.\n"
              "The bear then uses your remains as a wall to block the doorway you entered from.\n"
              "Lesson 1: Do not use bears.")
    else:
      return (INVALID)
  elif text == "LOOK BEAR":
    return ("The bear has golden brown fur and a red-tethered shirt on.\n"
            "The bear looks at you.")
  elif text == "USE KNIFE":
    if caveObject.bearExists():
      moveObject.changeLocation(6)
      return ("You try to fight the bear using the kitchen knife.\n"
              "You manage to slash the bear in its face.\n"
              "The bear gets angry and takes you down.\n"
              "In a desperate effort, you stab the bear in its torso.\n"
              "The bear only gets angrier, and mauls you to death furiously.\n"
              "Lesson 2: Do not fight bears with small weapons.")
    else:
      return (INVALID)
  elif text == "USE AXE":
    if caveObject.bearExists():
      moveObject.changeLocation(6)
      return ("You try to swing your axe at the bear's head, but the bear moved too fast.\n"
              "Your swing instead hits the body, it cleaves the bear only a little.\n"
              "The bear stands up, and mauls your arm that is holding the axe and knocks you down.\n"
              "The bear continues to maul you to death.\n"
              "Lesson 3: Do not fight bears with melee weapons.\n")
    else:
      return (INVALID)
  elif text == "USE HONEY":
    if (caveObject.bearExists() and not kitchenObject.honeyExists()):
      caveObject.killBear()
      scoreObject.addOne()
      return ("You go pour the honey down the hole, miraculously the honey falls out of the jar like water.\n"
              "You keep the jar. You step back.\n"
              "The bear chases after the honey, and you watch from afar.\n"
              "The bear falls down the hole, screaming \"HONEEYYYY!!!!\"")
    else:
      return (INVALID)
  elif text == "TAKE WATER":
    if caveObject.bearExists():
      return ("You don't have anything to take the water with.")
    elif not caveObject.waterExists():
      return ("There is no more water to take.")
    else:
      caveObject.takeWater()
      scoreObject.addOne()
      return ("You take the water and put it in the jar. You now have WATER.")
  elif text == "LOOK WATER":
    if caveObject.waterExists():
      return ("You see some dirty lookin' water. It looks dirtier than Dirty Dan.")
    else:
      return ("You see some remnants of the water left behind, not enough to grasp any in a jar.")
  else:
    return (INVALID)

def lab(entry):
  text=entry
  text=text.upper()
  if text =="USE COMPUTER":
    if labObject.computerOn():
      labObject.createPaper()
      labObject.shutDown()
      return ('You go to the computer that is on.\n'
              'You see on the screen \'Press Any Key.\'\n'
              'You search for the Any key, but are unable to find it.\n'
              'You get thirsty, so you press the tab button to put it on your tab.\n'
              'Instead of giving you a drink as you were hoping for, it prints out a PAPER.'
              "The computer seems to turn off. You try to turn it on, but it won't turn on. It seems to be broken.")
    else:
      return ("You try using the computers, but they don't work.")
  elif text=="LOOK COMPUTER":
    if labObject.computerOn():
      return ("You see on the screen \'Press Any Key.\'")
    else:
      return ("The computer is off.")
  elif text == "TAKE COMPUTER":
    return ("A good idea.... if it weren't trapped in glass cases.")
  elif text == "LOOK TABLE":
    return ("You move over to the table, brushing away all the destroyed peices of paper.\n"
            "However, you find a couple of peices you can read.\n"
            "One talks about 'their progress with the test subject has yeilded great results so far'.\n"
            "But as you keep going on down the line, it gets worse and worse.\n"
            "Until you get to one last paper that reads:\n"
            "'There's only one way to stop our monster, but it's already too late'.\n"
            "Oooo, ominous.")
  elif text =="USE TABLE":
    return ("You rest on the table.")
  elif text == "TAKE TABLE":
    return ("Not a bad idea... Wait, where the heck am I going to take this?")
  elif text=="LOOK PAPER":
    if labObject.paperExists():
      return ("Printed on the paper is ['1', '0', '*'].")
    else:
      return (INVALID)
  elif text=="TAKE PAPER":
    if labObject.paperExists():
      labObject.paperGot()
      scoreObject.addOne()
      return ("You take the paper that has printed on it: ['1', '0', '*'].")
    else:
      return (INVALID)
  elif text == "USE PAPER":
    if labObject.paperGot():
      return ("You read \"['1', '0', '*']\"")
  elif text=="MOVE UP":
    moveObject.changeLocation(5)
    return ("You proceed up the stairs.")
  elif text =="LOOK UP":
    return ("Oh, look a trapdoor.")

  elif text == 'HELP':
    return (HELP)
  elif text=="MOVE SOUTH":
    moveObject.changeLocation(3)
    return ("You go back to the cave.")
  elif text =="LOOK SOUTH":
    return ("That's the cave you came from.")
  else:
    return (INVALID)

def final(entry):
  text = entry
  text=text.upper()
  if text == "USE PAPER":
    if labObject.paperGot():
        scoreObject.addOne()
        moveObject.changeLocation(6)
        return ("You take out the paper you got back at the labs.\n"
                "As soon as you do, the monster shouts loudly: 'Is that what I think it is?!'\n"
                "You nod and crumple the paper up, tossing it at the monster's mouth.\n"
                "The monster screams loudly, the paper easily dropping into the monster's mouth.\n"
                "As the paper gets swallowed, the monster's gut begins to churn, the Tokenizer reeling in pain.\n"
                "Suddenly, it's gut begins to expand, getting to large that it bursts!\n"
                "The sudden force of wind makes you cover up your face. As you look back up, the Tokenizer is gone!\n"
                "All that remains of him is just some lame gold token- Oh hey! It's gold! I bet that could sell nicely!\n"
                "You happily put the gold token in your pocket and start to walk forward, nothing in your way now.\n"
                "All in all, you came out richer than you were before!")
    else:
      return (INVALID)

  elif text == "LOOK TOKENIZER":
    return ("Before you stands a huge hulk of monster.\n"
            "It's green, with large sharp teeth, its giant hands holding its decorated parse tree")
  elif text == "USE TOKENIZER":
    moveObject.changeLocation(6)
    return ("As you try to do something, not exactly sure what, with the monster, the monster smashes you with his parse tree.")
  elif text == "TAKE TOKENIZER":
    moveObject.changeLocation(6)
    return ("As you try to grab it, the monster smashes you with his parse tree.")
  elif text == "USE WATER":
    if not caveObject.waterExists():
      moveObject.changeLocation(6)
      return ("You take out the jar of water you got back at the caves, and toss it at the Tokenizer.\n"
              "As the jar shatters against it, the Tokenizer screams in pains.\n"
              "'Im melting!!' it shouts for a while, yelling in agony, stomping about.\n"
              "But suddenly, it stops. Nothing really happened to it.\n"
              "Once it realizes what happend, it takes his parse tree and smashes you.")
    else:
      return (INVALID)
  elif (text == "USE AXE"):
    if kitchenObject.axeExists():
      return ("Now's not the time to be using imaginary weapons!")
    else:
      moveObject.changeLocation(6)
      return ("You take out your bladed weapon and hold it up to the Tokenizer, warning it not to come any closer.\n"
              "The Tokenizer just laughs and brings its parse tree down on your head, crushing you.")
  elif (text == "USE KNIFE"):
    if kitchenObject.knifeExists():
      return ("Now's not the time to be using imaginary weapons!")
    else:
      moveObject.changeLocation(6)
      return ("You take out your bladed weapon and hold it up to the Tokenizer, warning it not to come any closer.\n"
              "The Tokenizer just laughs and brings its parse tree down on your head, crushing you.")
  elif text == "HELP":
    return ("Nope, no way. I am not helping with this giant monster. You're on your own.")
  elif text == "MOVE DOWN":
    moveObject.changeLocation(4)
    return ("You take one look at the giant Tokenizer and shake your head, saying 'Nope' as you retreat back into the Labs\n"
            "as the Tokenizer shouts back after you 'Wait we weren't finished yet!!'")
  elif text == "LOOK DOWN":
    return ("Sweet, sweet ground!")
  else:
    return (INVALID)
