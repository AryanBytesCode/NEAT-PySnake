import pygame
import sys
import numpy as np 
import random

# Define constants
GRID_WIDTH = 5
GRID_HEIGHT = 5
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
        # initalize gameState
        self.snakeGameState = np.zeros((GRID_HEIGHT,GRID_WIDTH))
        # spawn
        self.snakeGameState[self.head_y, self.head_x] = 1
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
            self.die()
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
            #self.die()
            ...
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
            self.fruit_x = random.randint(0, GRID_WIDTH-1)
            self.fruit_y = random.randint(0, GRID_HEIGHT-1)
            # check if the random location is part of the snake
            isOccupied = False
            for tile in self.locations:
                if tile[0] == self.fruit_x and tile[1] == self.fruit_y:
                    isOccupied = True
        
    def die(self):
        print("Snake died")
        print("Score: "+ str(self.snakeSize))
        self.__init__()
        ...
    def see(self):
        # Snake length : 1
        self.AI_Input_length = self.snakeSize
        # the whole gameState : 5*5*2 = 50
        self.AI_Input_gameState = self.snakeGameState 
        # distance of head to fruit as a 2d array : 2
        distance = np.array([self.head_x,self.head_y]) - np.array([self.fruit_x, self.fruit_y])
        self.AI_Input_distance = distance.tolist()
        # position of the head : 2
        self.AI_Input_head = [self.head_x, self.head_y]


        # total input variables : 55
        ...

def updateGlobalGameState():
    # set everything to zero
    globalGameState = np.zeros((GRID_HEIGHT,GRID_WIDTH))
    
    for snake in snakeList:
        # add snake tiles
        for tile in snake.locations:
            globalGameState[tile[1], tile[0]] = 1

        # add fruit
        globalGameState[snake.fruit_y, snake.fruit_x] = 2
    return globalGameState
    ...

# Spawn snakes
numberOfSnakes = 1
snakeList = []
for i in range(numberOfSnakes):
    snakeList.append(snake())

# add travelLength for every snake
travelLengthList = []
for i in range(len(snakeList)):
    travelLengthList.append(0)




# Main game loop
running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for snake in snakeList:
                if event.key == pygame.K_UP:
                    snake.direction= [0,-1]
                elif event.key == pygame.K_DOWN:
                    snake.direction= [0,1]
                elif event.key == pygame.K_LEFT:
                    snake.direction= [-1,0]
                elif event.key == pygame.K_RIGHT:
                    snake.direction= [1,0]

    # Fill the background
    screen.fill(BACKGROUND_COLOR)



    # Move snakes
    for index, snake in enumerate(snakeList):
        travelLengthList[index] += snake.speed * deltaTime
        snake.move(snake.direction, cellsToMove=int(travelLengthList[index]))
        if travelLengthList[index] > 1:
            travelLengthList[index] = 0


    # Make snakes see the changes
    for snake in snakeList:
        snake.see()

    # Update gameState
    gameState = updateGlobalGameState()
    
    # Draw gameState
    draw(gameState)


    
    #time.sleep(1)
    # Update the display
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000 # delta time in seconds since last frame, used for framerate-independent physics

# Quit Pygame
pygame.quit()
sys.exit()
