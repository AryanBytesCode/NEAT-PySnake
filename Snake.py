
from time import sleep
import pandas  as pd
import numpy as np 
import keyboard
import os
import random
import time
from colorama import Fore, Style
import sys

GAME_SPEED = 5

GRID_WITDH = 15
GRID_HEIGHT = 15

EMPTY_CELL = Style.RESET_ALL+ "[ ]"
SNAKE_CELL = Fore.BLUE + "[O]"
FRUIT_CELL = Fore.RED + "[X]"


gameState = np.zeros((GRID_HEIGHT,GRID_WITDH))




def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS or Linux
    else:
        os.system('clear')

class snake:
    def __init__(self):
        print("reset")
        self.head_x = random.randint(0,GRID_WITDH-1)
        self.head_y = random.randint(0, GRID_HEIGHT-1)
        print(self.head_y, self.head_x)
        self.direction = [1,0]
        self.snakeSize = 1
        self.speed = 2          ## two cells per second
        self.locations = []     ## an empty list to hold all snake locations
        # spawn
        gameState[self.head_y, self.head_x] = 1
        # save head to snake locations
        self.locations.append([self.head_x, self.head_y])

        # add fruit location
        self.addnewFruit()
        ...
    def move(self, directionVector=[-1,0]):
        destination_x = directionVector[0] + self.head_x
        destination_y = directionVector[1] + self.head_y

        # Check if we will hit the walls and restart the snake
        if destination_x < 0 or destination_x > GRID_WITDH-1 or destination_y < 0 or destination_y > GRID_HEIGHT-1:
            self.__init__()
            # stop the rest of the function
            return
            ...  
        #newcellValue = gameState[destination_y, destination_x] 
        newcellValue = [destination_x, destination_y]
        
        
        if not newcellValue in self.locations and not newcellValue == [self.fruit_x, self.fruit_y]:
            #gameState[self.head_y, self.head_x] = 1
            # move
            
            # update the head
            self.head_x = destination_x
            self.head_y = destination_y


            # remove the tail from snake data
            tailLocations = self.locations.pop()
            # add new head to snake data
            self.locations.insert(0, [destination_x, destination_y])
            ...
        elif newcellValue in self.locations:
            self.die()
        elif newcellValue == [self.fruit_x, self.fruit_y]:
            self.grow()
            # add new head to snake data
            self.locations.insert(0, [destination_x, destination_y])
            # update head
            self.head_x = destination_x
            self.head_y = destination_y

        
        self.direction = directionVector
    
    def grow(self):
        self.snakeSize = self.snakeSize + 1
        self.addnewFruit()
        ...
    def addnewFruit(self):
        isOccupied = True
        while isOccupied: 
            self.fruit_x = random.randint(0, GRID_WITDH-1)
            self.fruit_y = random.randint(0, GRID_HEIGHT-1)

            # check if the random location is part of the snake
            isOccupied = False
            for tile in self.locations:
                if tile[0] == self.fruit_x and tile[1] == self.fruit_y:
                    isOccupied = True
        
    def die(self):
        ...


    



def left():
    newSnake.direction= [-1,0]
    #newSnake.move([-1,0])
    ...

def right():
    newSnake.direction= [1,0]
    #newSnake.move([1,0])
    ...

def down():
    newSnake.direction= [0,1]
    #newSnake.move([0,1])
    ...

def up():
    newSnake.direction= [0,-1]
    #newSnake.move([0,-1])
    ...


def on_key_press(event):
    key = event.name
    if key == "left":
        left()
    elif key == "right":
        right()
    elif key == "up":
        up()
    elif key == "down":
        down()



def updateGameState():
    # set everything to zero
    gameState = np.zeros((GRID_HEIGHT,GRID_WITDH))
    
    # add snake tiles

    for tile in newSnake.locations:
        gameState[tile[1], tile[0]] = 1


    # add fruit
    gameState[newSnake.fruit_y, newSnake.fruit_x] = 2
    return gameState
    ...

def draw(state):

    #print(newSnake.head_x, newSnake.head_y)
    
    def codeToString(code):
        if code == 0:
            return EMPTY_CELL
        elif code == 1:
            return SNAKE_CELL
        elif code == 2:
            return FRUIT_CELL

    currentLine = 0
    lineString = ""
    while  currentLine < GRID_HEIGHT:
        row = state[currentLine, :]
        for i in range(len(row)):
            lineString = lineString + codeToString(row[i]) 
        print(lineString)
        lineString = ""
        currentLine = currentLine + 1
        ...


# run every frame
def update():
    clear_screen()
    print("Score: " + str(newSnake.snakeSize))
    global start_time
    end_time = time.time()
    last_frame_time = end_time - start_time
    #print(last_frame_time)
    second_per_cell = 1 / newSnake.speed
    # move the snake along its head direction
    if last_frame_time * GAME_SPEED >= second_per_cell:
        newSnake.move(newSnake.direction)
        #print("asdasdasd")
        start_time = end_time

    draw(updateGameState())

    




# setup

keyboard.on_press(on_key_press)

newSnake = snake()



global start_time
start_time = time.time()
while True:
   

    
    update()



    sleep(0.1)

#keyboard.wait('esc')
