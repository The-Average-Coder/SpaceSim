import pygame
import ctypes
import math

pygame.init()

ctypes.windll.user32.SetProcessDPIAware()
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Space Sim")

ORANGE = (255, 200, 0)
AQUA = (0, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
YELLOW = (255, 255, 0)
MAGENTA = (255, 150, 255)
VIOLET = (200, 0, 200)


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
    CelestialObject(MAGENTA, 40, 12_000_000_000, 700, 0, 0, 100_000_000_000)
]

inverseScaleFactor = 4

relativeCelestialObject = celestialObjects[0]

cameraPos = pygame.Vector2(0, 0)
centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                running = False

    cameraPos = relativeCelestialObject.position

    for i in celestialObjects:
        for j in celestialObjects:
            if i == j:
                continue
            distance = math.hypot(i.position.x-j.position.x,
                                  i.position.y-j.position.y)
            force = 0.00000000006743015 * ((i.mass * j.mass) / distance**2)
            radians = math.atan2(j.position.y - i.position.y,
                                 j.position.x - i.position.x)
            i.applyForce(force, radians)
        i.simulate()
    """
        distance = math.hypot(star.position.x-planet.position.x,
                              star.position.y-planet.position.y)
        force = 0.00000000006743015 * ((star.mass * planet.mass) / distance**2)

        starRadians = math.atan2(
            planet.position.y - star.position.y, planet.position.x - star.position.x)
        planetRadians = math.atan2(
            star.position.y - planet.position.y, star.position.x - planet.position.x)

        star.applyForce(force, starRadians)
        planet.applyForce(force, planetRadians)

        star.simulate()
        planet.simulate()
    """
    screen.fill((0, 0, 0))

    for i in celestialObjects:
        pygame.draw.circle(screen, i.colour, ((i.position.x -
                           cameraPos.x) / inverseScaleFactor + centre.x, (i.position.y - cameraPos.y) / inverseScaleFactor + centre.y), i.radius / inverseScaleFactor)
    """
    pygame.draw.circle(screen, (255, 0, 0),
                       star.position - cameraPos + centre, star.radius)
    pygame.draw.circle(screen, (0, 0, 255),
                       planet.position - cameraPos + centre, planet.radius)
    """
    pygame.display.flip()

    pygame.time.Clock().tick(120)


pygame.quit()
