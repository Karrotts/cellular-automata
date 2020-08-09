import cell
from PIL import Image, ImageDraw

# default colors for island
water_color = (128, 213, 255)
sand_color = (255, 221, 128)
grass_color = (72, 217, 127)

def main():
    # generate basic island
    island_grid = cell.generate((50, 50), 30, 5)

    # check if tile is near water if it is make it a sand tile
    for i in range(len(island_grid)):
        for j in range(len(island_grid[0])):
            if island_grid[i][j] == 0 and cell.find_neighbors(island_grid, (i, j)) >= 1:
                island_grid[i][j] = .5

    save_png(island_grid, 'images/island.png')

def save_png(grid, file_name):
    # calculate size of grid
    size = (len(grid), len(grid[0]))

    image = Image.new('RGB', size, grass_color)

    # iterate through grid and draw walls
    for i in range(size[0]):
        for j in range(size[1]):
            # draw sand or water tiles
            if grid[i][j] == 1:
                ImageDraw.Draw(image).point((i, j), water_color)
            if grid[i][j] == .5:
                ImageDraw.Draw(image).point((i, j), sand_color)

    # save image as png
    image.save(file_name, 'png')
    


if __name__ == "__main__":
    main()