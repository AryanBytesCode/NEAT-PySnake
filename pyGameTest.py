import pygame
import sys
import numpy as np 
import random
import time

# Define constants
GRID_WIDTH = 30
GRID_HEIGHT = 30
TILE_SIZE = 10
GAP = 2
CANVAS_SIZE_X = GRID_WIDTH * TILE_SIZE + GAP * GRID_WIDTH
CANVAS_SIZE_Y = GRID_HEIGHT * TILE_SIZE + GAP * GRID_HEIGHT
BACKGROUND_COLOR = (154,204,153)  # Green
TILE_COLOR = (154,204,153)          # Black
SNAKE_COLOR = (0,0,0)
FRUIT_COLOR = (255,0,0)




# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
deltaTime = 0


# Initialize gameState
gameState = np.zeros((GRID_HEIGHT,GRID_WIDTH))
travelLength = 0

# Create the screen with the modified size
screen = pygame.display.set_mode((CANVAS_SIZE_X, CANVAS_SIZE_Y))
pygame.display.set_caption("10x10 Tile Grid")


def draw(state):

    def codeToColor(code):
        if code == 0:
            return TILE_COLOR
        elif code == 1:
            return SNAKE_COLOR
        elif code == 2:
            return FRUIT_COLOR


    #pygame.draw.rect(screen, TILE_COLOR, (X, y, TILE_SIZE, TILE_SIZE))
        
    for y in range(GRID_HEIGHT):
         for x in range(GRID_WIDTH):
             ty = y+1 # to adjust for the 0 index
             tx = x+1 # to adjust for the 0 index
             # Calculate coordinates
             cor_x = tx * GAP + (tx-1) * TILE_SIZE   
             cor_y = ty * GAP + (ty-1) * TILE_SIZE
             color = codeToColor(gameState[y,x])
             # Draw rectangle
             pygame.draw.rect(screen, color, (cor_x, cor_y, TILE_SIZE, TILE_SIZE))
                
class snake:
    def __init__(self):
        self.head_x = random.randint(0,GRID_WIDTH-1)
        self.head_y = random.randint(0, GRID_HEIGHT-1)
        #print(self.head_y, self.head_x)
        self.direction = [1,0]
        self.snakeSize = 1
        self.speed = 8          ## abstract length per second
        self.locations = []     ## an empty list to hold all snake locations
        # spawn
        gameState[self.head_y, self.head_x] = 1
        # save head to snake locations
        self.locations.append([self.head_x, self.head_y])

        # add fruit location
        self.addnewFruit()
        ...
    def move(self, directionVector=[-1,0], cellsToMove=1):
        destination_x = directionVector[0]*cellsToMove + self.head_x
        destination_y = directionVector[1]*cellsToMove + self.head_y

        # Check if we will hit the walls and restart the snake
        if destination_x < 0 or destination_x > GRID_WIDTH-1 or destination_y < 0 or destination_y > GRID_HEIGHT-1:
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
        print("Snake")
        print(self.head_x, self.head_y)
    
    def grow(self):
        self.snakeSize = self.snakeSize + 1
        self.addnewFruit()
        ...
    def addnewFruit(self):
        isOccupied = True
        while isOccupied: 
            self.fruit_x = random.randint(0, GRID_WIDTH-1)
            self.fruit_y = random.randint(0, GRID_HEIGHT-1)
            print("new fruit baby")
            print(self.fruit_x, self.fruit_y)
            # check if the random location is part of the snake
            isOccupied = False
            for tile in self.locations:
                if tile[0] == self.fruit_x and tile[1] == self.fruit_y:
                    print("oops")
                    isOccupied = True
        
    def die(self):
        ...

def updateGameState():
    # set everything to zero
    gameState = np.zeros((GRID_HEIGHT,GRID_WIDTH))
    
    # add snake tiles
    for tile in newSnake.locations:
        gameState[tile[1], tile[0]] = 1

    # add fruit
    gameState[newSnake.fruit_y, newSnake.fruit_x] = 2
    return gameState
    ...

# Spawn Snake
newSnake = snake()


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                newSnake.direction= [0,-1]
            elif event.key == pygame.K_DOWN:
                newSnake.direction= [0,1]
            elif event.key == pygame.K_LEFT:
                newSnake.direction= [-1,0]
            elif event.key == pygame.K_RIGHT:
                newSnake.direction= [1,0]

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # move snake
    travelLength += newSnake.speed * deltaTime
    #print(travelLength)
    newSnake.move(newSnake.direction, cellsToMove=int(travelLength))
    if travelLength > 1:
        travelLength = 0
    
    # Update gameState
    gameState = updateGameState()

    # Draw gameState
    draw(gameState)


    
    #time.sleep(1)
    # Update the display
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000 # delta time in seconds since last frame, used for framerate-independent physics

# Quit Pygame
pygame.quit()
sys.exit()
