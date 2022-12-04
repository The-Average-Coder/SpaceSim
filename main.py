import pygame
import ctypes
import math

pygame.init()

ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1800
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Sim")

ORANGE = (255, 200, 0)
AQUA = (0, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
YELLOW = (255, 255, 0)
MAGENTA = (255, 150, 255)
VIOLET = (200, 0, 200)
WHITE = (255, 255, 255)

class CelestialObject:
    def __init__(self, colour, radius, mass, xPos, yPos, initialXForce, initialYForce):
        self.mass = mass
        self.radius = radius
        self.colour = colour
        self.position = pygame.Vector2(xPos, yPos)
        self.accelX = 0
        self.accelY = 0
        self.applyXYForce(initialXForce, initialYForce)

    def applyForce(self, force, direction):
        distanceX = math.cos(direction)
        distanceY = math.sin(direction)
        forceX = force * distanceX
        forceY = force * distanceY
        self.applyXYForce(forceX, forceY)

    def applyXYForce(self, forceX, forceY):
        self.accelX += forceX / self.mass
        self.accelY += forceY / self.mass

    def simulate(self):
        self.position.x += self.accelX
        self.position.y += self.accelY


celestialObjects = [
    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 0, 0, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 1000, 0, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 2000, 0, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 1800, 0, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 1500, 0, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 1200, 0, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 700, 0, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 5000, 0, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 6000, 0, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 7000, 0, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 6800, 0, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 6500, 0, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 6200, 0, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 5700, 0, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, -5000, 0, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, -4000, 0, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, -3000, 0, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, -3200, 0, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, -3500, 0, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, -3800, 0, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, -4300, 0, 0, 100_000_000_000),


    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 0, 5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 1000, 5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 2000, 5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 1800, 5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 1500, 5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 1200, 5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 700, 5000, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 5000, 5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 6000, 5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 7000, 5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 6800, 5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 6500, 5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 6200, 5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 5700, 5000, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, -5000, 5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, -4000, 5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, -3000, 5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, -3200, 5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, -3500, 5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, -3800, 5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, -4300, 5000, 0, 100_000_000_000),


    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 0, -5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 1000, -5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 2000, -5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 1800, -5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 1500, -5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 1200, -5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 700, -5000, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, 5000, -5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, 6000, -5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, 7000, -5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, 6800, -5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, 6500, -5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, 6200, -5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, 5700, -5000, 0, 100_000_000_000),

    CelestialObject(ORANGE, 100, 1_500_000_000_000_000, -5000, -5000, 0, 0),
    CelestialObject(AQUA, 30, 6_000_000_000, -4000, -5000, 0, 50_000_000_000),
    CelestialObject(RED, 15, 4_000_000_000, -3000, -5000, 0, 23_000_000_000),
    CelestialObject(VIOLET, 18, 4_300_000_000, -3200, -5000, 0, 26_000_000_000),
    CelestialObject(GREEN, 20, 4_500_000_000, -3500, -5000, 0, 30_000_000_000),
    CelestialObject(YELLOW, 25, 5_000_000, -3800, -5000, 0, 40_000_000),
    CelestialObject(MAGENTA, 40, 10_000_000_000, -4300, -5000, 0, 100_000_000_000),
]

inverseScaleFactor = 10

relativeCelestialObject = celestialObjects[0]

cameraPos = pygame.Vector2(0, 0)
centre = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clickedObjects = [j for j in celestialObjects if j.rect.collidepoint(pos)]
            if len(clickedObjects) > 0:
                relativeCelestialObject = clickedObjects[0]
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                running = False
            elif i.key == pygame.K_RIGHT:
                relativeCelestialObject = celestialObjects[(celestialObjects.index(relativeCelestialObject) + 1) % len(celestialObjects)]
            elif i.key == pygame.K_LEFT:
                relativeCelestialObject = celestialObjects[(celestialObjects.index(relativeCelestialObject) - 1) % len(celestialObjects)]

    cameraPos = relativeCelestialObject.position

    for i in celestialObjects:
        for j in celestialObjects:
            if i is j:
                continue
            distance = math.hypot(i.position.x-j.position.x, i.position.y-j.position.y)
            force = 0.00000000006743015 * ((i.mass * j.mass) / distance**2)
            radians = math.atan2(j.position.y - i.position.y, j.position.x - i.position.x)
            i.applyForce(force, radians)
        i.simulate()

    screen.fill((0, 0, 0))

    for i in celestialObjects:
        i.rect = pygame.draw.circle(screen, i.colour, ((i.position.x - cameraPos.x) / inverseScaleFactor + centre.x, (i.position.y - cameraPos.y) / inverseScaleFactor + centre.y), i.radius / inverseScaleFactor)
    
    pygame.display.flip()

    pygame.time.Clock().tick(120)


pygame.quit()
