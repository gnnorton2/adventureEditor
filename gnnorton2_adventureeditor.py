# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:30:12 2024

@author: gnoel
"""

import json

def main():
#Runs the main loop
   # game = getDefaultGame()
    game = getDefaultGame()
    keepGoing = True
    
    while keepGoing:
        userChoice = getUserChoice()
#        userChoice = getUserChoice()
#Calls a menu
#	0-5, exit game, play default game, load game, save game, edit node, play game 
        if userChoice == ("0"):
            keepGoing = False
        elif userChoice == ("1"):
            print("Play default game.") 
            #game = getDefaultGame()
        elif userChoice == ("2"):
            print("Loaded a game file")
            game = loadGame()
        elif userChoice == ("3"):
            print("Save the current game")
            saveGame(game)
        elif userChoice == ("4"):
            #editNode
            print("Edit or add node")
            game = editNode(game)
        elif userChoice == ("5"):
            playGame(game)
        else:
            print("I think you clicked the wrong button.")
#Sends control to other parts of the program

def getUserChoice():
#prints a menu of user options
    print("""
          0) Exit the game
          1) Load default
          2) Load game file
          3) Save current game
          4) Edit/Add Node
          5) Play current game
          """)
    userChoice = input("Your choice: \n")
    return userChoice
#	print(0-5, exit game, play default game, load game, save game, edit node, play game)
#if (0-5) # make an if/elif for each one) 
#	do whatever the choice is
#else:
#	repeats if input is invalid
#returns a valid menu choice

def playGame(game):
#runs the game
    #(description, menuA, menuB, nodeA, nodeB) = game[currentGame]
    currentNode = "Start"
    keepGoing = True
    
    while keepGoing:
        currentNode = playNode(game, currentNode)
        if currentNode == "Quit":
            keepGoing = False
        #else:
            #currentNode = playNode(game, currentNode)
#Keeps going until next node is "quit"

def playNode(game, currentNode):
    if currentNode in game.keys():
        (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
        print(f""" 
        {desc}
        1) {menuA}
        2) {menuB}""")
      #  3) {nodeA}
      #  4) {nodeB}
       #       """)
        response = input("What will you choose? ")
        if response == ("1"):
            currentNode = game[currentNode][2]
        elif response == ("2"):
            currentNode = game[currentNode][4]
        else:
            print("Wrong input")
    return currentNode
#given the game data and a node,
#plays out the node
#returns the next node

def getDefaultGame():
#keepgoing = true
    game = {"Start": ["default start node", "Start Over", "Start", "Quit game", "Quit"]}
            
    return game

def editNode(game):
#given the current game structure...
   print("Editing nodes")
   print(json.dumps(game, indent=2))
   
   for nodeName in game.keys():
       print(f"{nodeName}")

   newNodeName = input("Enter a new node name")
   if newNodeName in game.keys():
           newContent = game[newNodeName]
   else:
       newContent= ("", "", "", "", "")
   (description, menuA, menuB, nodeA, nodeB) = newContent
   newDesc = editField("description", description)
   newMenuA = editField("Menu A", menuA)        # <-- do this for menu A, menuB, Noda A, Node B
   newMenuB = editField("Menu B", menuB)
   newNodeA = editField("Node A", nodeA)
   newNodeB = editField("Node B", nodeB)
   game[newNodeName] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]
#	print dictionary
#list all the current node names
#get a node name
    
#if that node exists
#copy that node to newNode
#otherwise...
#create newNode with empty data
   return game
#use editField() to allow user to edit each node
#return the now edited newNode

def editField(prompt, currentVal):
#get a field name
    newVal = input(f"{prompt} ({currentVal}): ")
    if newVal == "":
        newVal = currentVal
        
    return newVal
    
#print the field's current value
#if the user presses 'enter' immediately
#retain the current value
#otherwise...
#use the new value

def saveGame(game):
    fileName = "game.json"
#save the game to a data file
    outFile = open(fileName, "w")
    print(json.dumps(game, indent=2))
    json.dump(game, outFile, indent=2)
    outFile.close()
    print(json.dumps(game, indent=2))
#	json.dump(game.dat, outFile, indent = 2)
#you can preset the file name (eg 'game.dat')

#print the current game dictionary in human-readable format
#Save the file in JSON format
#	outFile.close()

def loadGame():
    fileName = "game.json"
    inFile = open(fileName, "r")
#presume there is a data file named 'game.dat' in the current directory
#outFile = open("game.dat", "r")
#open that file
    game = json.load(inFile)
    inFile.close()
    return game
#load the data into the game object
#return that game object

main()