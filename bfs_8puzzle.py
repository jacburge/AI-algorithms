import numpy as np 
import sys
import random
from random import shuffle
from datetime import datetime
random.seed(datetime.now())

def welcome():
    print("Welcome to the 8-puzzle simulation. " + \
        "I'm pretty artifical as far as intelligence goes. " + \
        "Let's get started, shall we?")
    return

welcome()

### Bring in system arguments
goalState = [0,1,2,3,4,5,6,7,8]
_,method,*entry = sys.argv
initState = []
for i in entry:
    initState.append(int(i))


### Make sure the input is valid
# count = 0
# def InversionsCount(x):
#     global count
#     x = [a for a in x if a != 0]
#     midsection = round(len(x) / 2)
#     leftArray = x[:midsection]
#     rightArray = x[midsection:]
#     if len(x) > 1:
#         InversionsCount(leftArray)
#         InversionsCount(rightArray)
#         i, j = 0, 0
#         a = leftArray; b = rightArray
#         for k in range(len(a) + len(b) + 1):
#             if a[i] <= b[j]:
#                 x[k] = a[i]
#                 i += 1
#                 if i == len(a) and j != len(b):
#                     while j != len(b):
#                         k +=1
#                         x[k] = b[j]
#                         j += 1
#                     break
#             elif a[i] > b[j]:
#                 x[k] = b[j]
#                 count += (len(a) - i)
#                 j += 1
#                 if j == len(b) and i != len(a):
#                     while i != len(a):
#                         k+= 1
#                         x[k] = a[i]
#                         i += 1                    
#                     break   

# def check_if_solvable():
#     InversionsCount(initState[:])
#     if count%2 == 0:
#         print('Sorry, that is not a solvable puzzle!')
#         exit()
#     else:
#         return True
# check_if_solvable()

def goalTest(state):
    if state == goalState:
        return True
    else:
        return False

if goalTest(initState):
    print("Hey, no fair playing with a solved game! Try again.")
    exit()

### Initialize game
def initialize_game():
    print("Initial board:")
    print(initState)
    blank = initState.index(0)
    print('Goal state:')
    print(goalState)
    print('Initial board as matrix:')
    print(np.array(initState).reshape(3,3))
    print('Index location of blank space:')
    print(blank)

initialize_game()

# #Define helper functions to move the blank space
def up(state):
#  blank moves 3 steps left
    moveBlank = state[:]
    i = moveBlank.index(0)
    moveBlank[i], moveBlank[i-3] = moveBlank[i-3], moveBlank[i]
    return moveBlank

def down(state):
#  blank moves 3 steps right
    moveBlank = state[:]
    i = moveBlank.index(0)
    moveBlank[i], moveBlank[i+3] = moveBlank[i+3], moveBlank[i]
    return moveBlank

def left(state):
#  blank moves 1 step left
    moveBlank = state[:]
    i = moveBlank.index(0)
    moveBlank[i], moveBlank[i-1] = moveBlank[i-1], moveBlank[i]
    return moveBlank

def right(state):
#  blank moves 1 step right
    moveBlank = state[:]
    i = moveBlank.index(0)
    moveBlank[i], moveBlank[i+1] = moveBlank[i+1], moveBlank[i]
    return moveBlank

# ### Identify adjacent neighbors of the blank
def findNeighbors(state):
    neighborState = {}
    i = state.index(0)
    #Check edges
    if i not in (0,1,2): #up
        neighborState['up'] = up(state)
    if i not in (6,7,8): #down
        neighborState['down'] = down(state)
    if i not in (0,3,6): #left side
        neighborState['left'] = left(state)
    if i not in (2,5,8): #right
        neighborState['right'] = right(state)
    return neighborState

# ### Define the breadth first search algorithm to solve the game
def bfs(initState):
    print("Initial state...")
    print(initState)
    init = initState[:]
    frontier = [init]
    explored = []
    neighbors = []
    # path_to_goal = []
    cost_of_path = 0
    path_graph = ''
    while len(frontier) > 0:
        state = frontier[0]
        print('new state:')
        print(state)
        frontier.pop(0)
        explored.append(state)
        if goalTest(state):
            print("Success!")
            print("final State: ")
            print(state)
            print("path_to_goal: ")
            path_to_goal = list(path_graph.split(','))
            print(path_to_goal[1:])
            # print("neighbors: ")
            # print(neighbors)
            print("cost_of_path: ")
            print(len(path_to_goal)-1)
            return
        for path, neighbor in findNeighbors(state).items():
            if neighbor not in frontier and neighbor not in explored:
                frontier.append(neighbor)
                neighbors.append(path_graph + ',' + path)
        print("neighbors: ")
        print(neighbors)
        path_graph = neighbors[0]
        # path_to_goal.append(neighbors[0])
        neighbors.pop(0)
        cost_of_path += 1
        # print('cost of path:')
        # print(cost_of_path)
        # print('path:')
        # print(path_to_goal)
        if cost_of_path == 100:
            print('Did you know Breadth First Search can take 350 YEARS to run through a tree of depth 16?!')
            print('Sorry, this might not be a solvable puzzle...')
            return
    return 'Failure'

bfs(initState)
