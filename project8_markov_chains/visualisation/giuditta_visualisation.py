import numpy as np
import cv2
from faker import Faker
from numpy.random import choice
import pandas as pd


TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
##..da..rcY.iw..##
##..mtY.qc..lsY.##
##..mzY.ph..lg..##
##..nz..ov..ybY.##
##..nt..ov..yb..##
##...............#
##..CgY.CpY.CnY..#
##..F#..F#..F#...#
##...............#
##############GG##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.customers = []
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split("\n")]
        self.xsize = len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros(
            (self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.tiles[0:32, 0:32]
        elif char == "G":
            return self.tiles[7 * 32 : 8 * 32, 3 * 32 : 4 * 32]
        elif char == "C":
            return self.tiles[2 * 32 : 3 * 32, 8 * 32 : 9 * 32]
        elif char == "F":
            return self.tiles[7 * 32 : 8 * 32, 0 * 32 : 1 * 32]
        elif char == "Y":
            return self.tiles[4 * 32 : 5 * 32, 2 * 32 : 3 * 32]
        elif char == "a":
            return self.tiles[6 * 32 : 7 * 32, 12 * 32 : 13 * 32]
        elif char == "b":
            return self.tiles[0 * 32 : 1 * 32, 4 * 32 : 5 * 32]
        elif char == "c":
            return self.tiles[2 * 32 : 3 * 32, 11 * 32 : 12 * 32]
        elif char == "d":
            return self.tiles[1 * 32 : 2* 32, 6 * 32 : 7 * 32]
        elif char == "e":
                return self.tiles[7 * 32 : 8 * 32, 11 * 32 : 12 * 32]
        elif char == "f":
                return self.tiles[4 * 32 : 5 * 32, 4 * 32 : 5 * 32]
        elif char == "g":
                return self.tiles[5 * 32 : 6 * 32, 4 * 32 : 5 * 32]
        elif char == "h":
                return self.tiles[1 * 32 : 2 * 32, 11 * 32 : 12 * 32]
        elif char == "i":
                return self.tiles[7 * 32 : 8 * 32, 10 * 32 : 11 * 32]
        elif char == "l":
                return self.tiles[7 * 32 : 8 * 32, 4 * 32 : 5 * 32]
        elif char == "m":
                return self.tiles[5 * 32 : 6 * 32, 6 * 32 : 7 * 32]
        elif char == "n":
                return self.tiles[6 * 32 : 7 * 32, 6 * 32 : 7 * 32]
        elif char == "o":
                return self.tiles[6 * 32 : 7 * 32, 5 * 32 : 6 * 32]
        elif char == "p":
                return self.tiles[2 * 32 : 3 * 32, 4 * 32 : 5 * 32]
        elif char == "q":
                return self.tiles[5 * 32 : 6 * 32, 11 * 32 : 12 * 32]
        elif char == "r":
                return self.tiles[4 * 32 : 5 * 32, 11 * 32 : 12 * 32]
        elif char == "t":
                return self.tiles[1 * 32 : 2 * 32, 3 * 32 : 4 * 32]
        elif char == "y":
                return self.tiles[3 * 32 : 4 * 32, 6 * 32 : 7 * 32]
        elif char == "s":
            return self.tiles[1 * 32 : 2 * 32, 5 * 32 : 6 * 32]
        elif char == "v":
            return self.tiles[3 * 32 : 4 * 32, 11 * 32 : 12 * 32]
        elif char == "z":
                return self.tiles[2 * 32 : 3 * 32, 3 * 32 : 4 * 32]
        elif char == "w":
                return self.tiles[3 * 32 : 4 * 32, 4 * 32 : 5 * 32]
        else:
            return self.tiles[32:64, 64:96]

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[
                    y * TILE_SIZE : (y + 1) * TILE_SIZE,
                    x * TILE_SIZE : (x + 1) * TILE_SIZE,
                ] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[
            OFS : OFS + self.image.shape[0], OFS : OFS + self.image.shape[1]
        ] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


if __name__ == "__main__":

    background = np.zeros((700, 1000, 3), np.uint8)
    tiles = cv2.imread("tiles.png")

    market = SupermarketMap(MARKET, tiles)

    while True:
        frame = background.copy()
        market.draw(frame)

        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == "q":
            break

    cv2.destroyAllWindows()

    market.write_image("supermarket.png")


"""
class Customer:


    def __init__(self, name, state, terrain_map, image, x, y):
        self.name = name
        self.state = state
        self.trans_probs = pd.read_csv("transition_matrix.csv")
        self.terrain_map = ___
        self.image = ___
        self.x = ___
        self.y = ___

    def draw(self, frame):
        xpos = OFS + self.x * TILE_SIZE
        ypos = ___
        frame[ypos:___, xpos: ___] = self.image
        # overlay the Customer image / sprite onto the frame




    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'


    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        loc_list = ['checkout','dairy', 'drinks', 'fruit','spices']
        initial_state = self.state
        weights = self.trans_probs[self.trans_probs['location'] == initial_state].to_numpy().tolist()
        new_state = np.random.choice(loc_list,1, weights)[0]

        return new_state



    def is_active(self):

        if self.state != 'checkout':
            return True
"""
