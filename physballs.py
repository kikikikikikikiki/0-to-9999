import pygame
import math as m
pygame.init()

main_surface = pygame.display.set_mode((1200, 800))
my_clock = pygame.time.Clock()

def draw_ball(itertat, color, vx, vy, gx, gy, veloy, velox, veloy2, velox2, siz):
    pygame.draw.circle(main_surface, color, [int(velox), int(veloy)], siz, 0)
    if itertat > 0:
        vy += gy*1j.real+gy*1j.imag
        vx += gx*1j.real+gx*1j.imag
        
        veloy -= vy.real
        velox -= vx.real
        velox2 = velox
        veloy2 = veloy
        
        color[0] +=2
        draw_ball(itertat-1, color, vx-0.1, vy-0.1, gx, gy, veloy2, velox2, veloy2, velox2, siz-1)
    else:
        color[0] = 0        

def gameloop():
    test = 0
    vely = 12
    velx = 12
    vely2 = vely
    velx2 = velx
    vy = 0
    vx = 0
    gy = 0.05 
    gx = 0.05
    itertat = 100
    siz = 100
    coloor = [0,0,0]
    while True:
        vy += gy
        vx += gx
        
        vely += vy
        velx += vx
        
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        main_surface.fill((10,10,10))
        if vely > 640:
            vely = 640
            vy = -(vy-0.5)
        if velx > 1040:
            velx = 1040
            vx = -(vx-0.5)
        draw_ball(itertat, coloor, vx, vy, gx, gy, vely, velx, vely2, velx2, siz)
        pygame.display.flip()
        my_clock.tick(60)

gameloop()
pygame.quit()
