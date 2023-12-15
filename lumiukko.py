import pygame


def alusta():
    pygame.init()
    naytto = pygame.display.set_mode((480, 640))
    return naytto


def piirra_lumiukko(naytto, x: int, y: int):
    pygame.draw.circle(naytto, (255,255,255), (x,y), 80)
    pygame.draw.circle(naytto, (255,255,255), (x,y-140), 60)
    pygame.draw.circle(naytto, (255,255,255), (x,y-240), 40)
	
lumiukko_x = 240
lumiukko_y = 420


NOPEUS = 0.2


naytto = alusta()


pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
   
    naytto.fill((0,0,0))
    lumiukko = piirra_lumiukko(naytto, lumiukko_x, lumiukko_y)


    pygame.display.flip()


    painetut_nappulat = pygame.key.get_pressed()
   
    if painetut_nappulat[pygame.K_LEFT]:
        lumiukko_x -= NOPEUS
    if painetut_nappulat[pygame.K_RIGHT]:
        lumiukko_x += NOPEUS
    if painetut_nappulat[pygame.K_DOWN]:
        lumiukko_y += NOPEUS
    if painetut_nappulat[pygame.K_UP]:
        lumiukko_y -= NOPEUS

