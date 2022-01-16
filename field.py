class Tile:
    def __init__(self):
        self.alive = 0

    def set_alive(self):
        self.alive = 1

    def set_dead(self):
        self.alive = 0

    def is_alive(self):
        return self.alive


class Field:
    def __init__(self, size):
        self.size = size
        self.table = [[Tile()] * size for _ in range(size)]

    def toggle_tile(self, x, y):
        if self.table[y][x].is_alive():
            self.table[y][x].set_dead()
        else:
            self.table[y][x].set_alive()

    def set_tile_alive(self, x, y):
        self.table[y][x].set_alive()

    def set_tile_dead(self, x, y):
        self.table[y][x].set_dead()

    def count_living_neighbours(self, x, y):
        res = self.table[(y - 1) % self.size][(x - 1) % self.size].is_alive() + \
              self.table[(y - 1) % self.size][x].is_alive() + \
              self.table[(y - 1) % self.size][(x + 1) % self.size].is_alive() + \
              self.table[y][(x - 1) % self.size].is_alive() + \
              self.table[y][(x + 1) % self.size].is_alive() + \
              self.table[(y + 1) % self.size][(x - 1) % self.size].is_alive() + \
              self.table[(y + 1) % self.size][x].is_alive() + \
              self.table[(y + 1) % self.size][(x + 1) % self.size].is_alive()
        return res

    def update(self):
        numeral_print = [[0] * self.size for _ in self.size]
        for x in range(self.size):
            for y in range(self.size):
                neighbours = self.count_living_neighbours(x, y)
                if neighbours == 3:
                    numeral_print[y][x] = 1
                elif neighbours < 2 or neighbours > 3:
                    numeral_print[y][x] = 0
        for x in range(self.size):
            for y in range(self.size):
                if numeral_print[y][x]:
                    self.set_tile_alive(x, y)
                else:
                    self.set_tile_dead(x, y)
