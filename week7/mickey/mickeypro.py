import math
import pygame

from pygame import Vector2

screen_size = Vector2(1400, 1050)
screen_center = screen_size // 2

reference_dict = {}

def rotate_on_pivot(image, angle, pivot, origin):
    
    surf = pygame.transform.rotate(image, angle)
    
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center = offset)
    
    return surf, rect

class SecondsHand:

    chain_length = -124

    def __init__(self, pivot, starting_angle = 0):

        self.pivot = pivot
        self.angle = 0

        offset = Vector2()
        offset.from_polar((self.chain_length, -starting_angle))

        self.pos = pivot + offset


    def update(self, dt):
        self.angle -= 0.1 

        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot, self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class MinuteHand:

    chain_length = -124

    def __init__(self, pivot, starting_angle = 0):

        self.pivot = pivot
        self.angle = 0

        offset = Vector2()
        offset.from_polar((self.chain_length, -starting_angle))

        self.pos = pivot + offset

        self.image_orig = reference_dict['week7/mickey/images/minuteshand']
        self.image = self.image_orig
        self.rect = self.image.get_rect(center = self.pos)

    def update(self, dt):
        self.angle -= 0.01666666667 

        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot, self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Clock:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = False

        self.screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)

        self.load_image('week7/mickey/images/mickey')

        self.minutehand = MinuteHand(screen_center, starting_angle = 30)

    def load_image(self, image_name, colorkey = None):
        image = pygame.image.load(f'{image_name}.png').convert()

        if colorkey is not None:
            image.set_colorkey(colorkey)

        reference_dict[image_name] = image

    def update(self, dt):
        self.minutehand.update(dt)

    def draw(self, surface):

        surface.fill('black')

        surface.blit(reference_dict['week7/mickey/images/mickey'], (0, 0))

        self.minutehand.draw(surface)

        pygame.display.flip()

    def run(self):

        self.running = True

        while self.running:

            dt = self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            self.update(dt)
            self.draw(self.screen)


if __name__ == '__main__':
    Clock().run()