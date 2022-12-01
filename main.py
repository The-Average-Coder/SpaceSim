import pygame
import ctypes
import math

pygame.init()

ctypes.windll.user32.SetProcessDPIAware()
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Space Sim")

ORANGE = (255, 200, 0)
AQUA = (0, 100, 255)
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
        print(self.accelX, self.accelY)
        self.position.x += self.accelX / 10
        self.position.y += self.accelY / 10


celestialObjects = [
    #star = CelestialObject(50, 10_000_000_000_000_000, 900, 500, 0, 0)
    #planet = CelestialObject(20, 1_000_000_000_000_000, 1200, 500, 0, -50_000_000_000_000_000)
    CelestialObject(ORANGE, 50, 250_000_000_000_000_000, 0, 0, 0, 0),
    CelestialObject(AQUA, 20, 1_000_000_000_000_000, 600,
                    0, 0, 540_000_000_000_000_000),
    CelestialObject(WHITE, 10, 7_000_000_000_000,
                    700, 0, 0, 3_000_000_000_000_000)
]


relativeCelestialObject = celestialObjects[1]

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
        pygame.draw.circle(screen, i.colour, i.position -
                           cameraPos + centre, i.radius)
    """
    pygame.draw.circle(screen, (255, 0, 0),
                       star.position - cameraPos + centre, star.radius)
    pygame.draw.circle(screen, (0, 0, 255),
                       planet.position - cameraPos + centre, planet.radius)
    """
    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.quit()
