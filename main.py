import pygame
from field import Field


class Game:
    def __init__(self, field_size):
        self.field_size = field_size

        pygame.init()
        self.screen = pygame.display.set_mode(size=(0, 0))
        self.SIZE = self.WIDTH, self.HEIGHT = self.screen.get_size()
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

        self.tile_size = self.HEIGHT // self.field_size
        self.margin = (self.HEIGHT % self.field_size) // 2
        self.left_margin = min(20, self.margin)

        self.field = Field(self.field_size)

    def draw_field(self):
        for x_num in range(self.field_size):
            for y_num in range(self.field_size):
                if self.field.get_tile_state(x_num, y_num):
                    pygame.draw.rect(self.screen, (0, 255, 0), (x_num * self.tile_size + self.left_margin,
                                                                y_num * self.tile_size + self.margin,
                                                                self.tile_size, self.tile_size))
                pygame.draw.lines(self.screen,
                                  (100, 100, 100),
                                  closed=False,
                                  points=((x_num * self.tile_size + self.left_margin,
                                           (y_num + 1) * self.tile_size + self.margin),
                                          (x_num * self.tile_size + self.left_margin,
                                           y_num * self.tile_size + self.margin),
                                          ((x_num + 1) * self.tile_size + self.left_margin,
                                           y_num * self.tile_size + self.margin)))
        pygame.draw.lines(self.screen,
                          (100, 100, 100),
                          closed=False,
                          points=((self.field_size * self.tile_size + self.left_margin,
                                   self.margin),
                                  (self.field_size * self.tile_size + self.left_margin,
                                   self.field_size * self.tile_size + self.margin),
                                  (self.left_margin,
                                   self.field_size * self.tile_size + self.margin)))

    def calculate_tile_coords(self, screen_x, screen_y):
        x = (screen_x - self.left_margin - 1) // self.tile_size
        y = (screen_y - self.margin - 1) // self.tile_size
        return x, y

    def run(self):
        finished = False
        time_is_going = False
        update_time = 100
        animtimer = 0
        while not finished:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    if event.key == pygame.K_SPACE:
                        if time_is_going:
                            time_is_going = False
                        else:
                            time_is_going = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    screen_x, screen_y = event.pos
                    if ((not time_is_going and
                         self.left_margin < screen_x <= self.left_margin + self.tile_size * self.field_size and
                         self.margin < screen_y <= self.margin + self.tile_size * self.field_size)):
                        tile_x, tile_y = self.calculate_tile_coords(screen_x, screen_y)
                        self.field.toggle_tile(tile_x, tile_y)
                elif event.type == pygame.MOUSEWHEEL:
                    pass

            if time_is_going:
                animtimer += self.clock.get_time()
                if animtimer >= update_time:
                    self.field.update()
                    animtimer = 0
            self.screen.fill((0, 0, 0))
            self.draw_field()
            pygame.display.flip()


if __name__ == '__main__':
    field_size = 0
    print("Введите длину стороны зацикленного квадратного поля от 10 до 100 (в клеточках).")
    while True:
        field_size = input()
        if field_size.isdigit():
            field_size = int(field_size)
            if 10 <= field_size <= 100:
                break
        print("Введите только одно число - длину стороны поля в клеточках от 10 до 100.")
    game = Game(field_size)
    game.run()
