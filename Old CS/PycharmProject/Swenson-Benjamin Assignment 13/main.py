import time
import sys

SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = True

# TODO: write all your code below this line
#
# put the line "if VERBOSE: printMaze(maze)"
# everytime you drop/retrieve a marker
#
def solve(maze, i, j):
    if
    if i < 0: return False
    if j < 0: return False

    if solve(maze, y+1, z): return True
    if solve(maze, y-1, z): return True
    if solve(maze, y, z+1): return True
    if solve(maze, y, z-1): return True

# TODO: write all your code above this line

def readMaze(maze):
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()

def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end="")
        print()
    time.sleep(SLEEPTIME)
    print()

def main():
    maze = []
    readMaze(maze)
    if not solve(maze, 1, 0):
        print("no solution is possible.")
    else:
        printMaze(maze)


main()



