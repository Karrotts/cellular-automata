from PIL import Image, ImageDraw
import random
import math
import datetime

def main():
    save_png(generate((200, 200), 50, 10), 'images/cellular_automata.png')

def generate(size, place_chance, smooth_cycles, seed=None):
    # set seed
    if not seed == None:
        random.seed(seed, version=2)
    else:
        random.seed(datetime.datetime.now(), version=2)

    # initialize grid
    grid = [[None for y in range(size[1])] for x in range(size[0])]

    # generate a grid with randomly placed ones and zeros
    for i in range(size[0]):
        for j in range(size[1]):
            # set walls
            if(i == 0 or i == size[0] - 1  or j == 0 or j == size[1] - 1):
                grid[i][j] = 1
            # randomly place walls
            else:
                if random.randint(1, 100) <= place_chance:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0

    # smooth to copy of grid
    for x in range(smooth_cycles):
        # create copy of grid
        grid_copy = list(map(list, grid))
        # interate through grid
        for i in range(size[0]):
            for j in range(size[1]):
                # find amount of neighbors
                neighbors = find_neighbors(grid, (i, j))
                # if a square has more than 4 neighbors than make it a wall else if it has less than 4 make it a tile
                if neighbors > 4:
                    grid_copy[i][j] = 1
                elif neighbors < 4:
                    grid_copy[i][j] = 0
        # set grid to the modified copy of grid to prevent bias
        grid = grid_copy

    # output grid
    return grid

def find_neighbors(grid, grid_pos):
    # initialize neighbors
    neighbors = 0
    # iterate through 3x3 grid around pixel
    for i in range(grid_pos[0] - 1, grid_pos[0] + 2):
        for j in range(grid_pos[1] - 1, grid_pos[1] + 2):
            # check if the grid pos is not an outer wall
            if (not i <= 0 and not i >= len(grid) - 1) and (not j <= 0 and not j >= len(grid[0]) - 1):
            # check if the neighbor is a wall, if it is increment the counter
                if grid[i][j] == 1 and not (i, j) == grid_pos:
                    neighbors += 1
            else:
                if not (i, j) == grid_pos:
                    neighbors += 1

    # return total neighbors
    return neighbors



def save_png(grid, file_name):
    # calculate size of grid
    size = (len(grid), len(grid[0]))

    # crate a new black/white image with a white background
    image = Image.new('1', size, 1)

    # iterate through grid and draw walls
    for i in range(size[0]):
        for j in range(size[1]):
            if grid[i][j] == 1:
                ImageDraw.Draw(image).point((i, j), 0)
    
    image.save(file_name, 'png')


if __name__ == "__main__":
    main()