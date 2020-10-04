import random
from time import sleep
import matplotlib.pyplot as plt

def make2dArray(cols,rows):
    return [[0 for i in range(cols)] for j in range(rows)]

def neighborscount(grid,x,y):
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows
            sum += grid[col][row]
    sum -= grid[x][y]
    return sum



def draw():
    global grid

    plt.imshow(grid, cmap="binary")
    plt.pause(0.001)

    next = make2dArray(cols,rows)
    if next == grid:
        print("Extinction")



    for i,n1 in enumerate(grid):
        for j,n2 in enumerate(n1):
            state = grid[i][j]
            sum = 0
            neighbors = neighborscount(grid,i,j)

            if state == 0 and neighbors == 3:
                next[i][j] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                next[i][j] = 0
            else:
                next[i][j] = state
    grid = next

fig = plt.figure(0)
fig.canvas.set_window_title('Conway\'s Game of Life')

cols = 50
rows = 50
generation = 0


extinction = False

grid = make2dArray(cols,rows)

for n1,i in enumerate(grid):
    for n2,j in enumerate(i):
        grid[n1][n2] = random.randint(0,1)

while True:
    print("\n")

    for row in grid:
        print(row)
    print("Genaration {}".format(generation))
    generation+=1

    draw()
plt.show()
