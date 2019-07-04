import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Purple Galaxy')
purplebg = pygame.image.load('PurpleGalaxyBGVG2019.png')
run = True
PlayerShip = pygame.image.load('PlayerSpaceshipVG2019.png')
MissilePIC = pygame.image. load('MissilesPGVG2019.png')
missiles = []
missileExists = False
clock = pygame.time.Clock()

def refreshScreen():
    win.blit(purplebg, (0,0))
    win.blit(PlayerShip, (player.x, player.y))
    pygame.display.update()
    for missile in missiles:
        missile.draw()


class projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1

    def draw(self):
        win.blit(MissilePIC, (self.x, self.y))

class playerShip(object):
    def __init__(self, x, y, sideVel, boostVel):
        self.x = x
        self.y = y
        self.sideVel = sideVel
        self.boostVel = boostVel


player = playerShip(218, 386, 5, 2)


while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    for missile in missiles:
        if missile.y > 0 and missile.y < 500:
            missile.y += missile.vel
        else:
            missiles.pop(missiles.index(missile))

    if keys[pygame.K_LEFT]:
        player.x -= player.sideVel
    if keys[pygame.K_RIGHT]:
        player.x += player.sideVel
    if keys[pygame.K_UP]:
        player.y -= player.boostVel
    if keys[pygame.K_DOWN]:
        player.y += player.boostVel
    if keys[pygame.K_SPACE]:
        missiles.append(projectile(player.x, player.y))
    refreshScreen()
