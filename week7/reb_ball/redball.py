import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False

clock = pygame.time.Clock()
x = 500
y = 500

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 25: y -= 20
        if pressed[pygame.K_DOWN] and y < 975: y += 20
        if pressed[pygame.K_LEFT] and x > 25: x -= 20
        if pressed[pygame.K_RIGHT] and x < 975: x += 20
        
        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)