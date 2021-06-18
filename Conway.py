import pygame
import numpy as np

randomRules=False
dead_color = (200, 200, 225)
alive_color = (0, 255, 25)
background_color = (0, 0, 0)
grid_color= (30, 30, 60)
pygame.display.set_caption("GameOfLife-CustomRules")

def update(surface, cur, sz,rulelive,ruledead):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]
        if (cur[r, c] == 1 and any( num_alive == i for i in rulelive)):
            nxt[r, c] = 1
            color = alive_color
        elif (cur[r, c] == 0 and any(num_alive == i for i in(ruledead))):
            nxt[r, c] = 1
            color = alive_color
        else:
            color = dead_color
        color = color if cur[r, c] == 1 else background_color
        pygame.draw.rect(surface, color, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def drawrandompatern(size):
    tab= np.random.randint(2,size=(size, size))
    return tab

#Funkcja generująca czarne wzory
def drawblack(size):
    tab=[]
    for y in range(size):
        row = []
        for x in range(size):
            row.append(1)
        tab.append(row)
    return tab

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array(drawrandompatern(21))
    pos = (49,49)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells


def main(dimx, dimy, cellsize,rulelive,ruledead,input):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    cells = init(dimx, dimy)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        surface.fill(grid_color)
        cells = update(surface, cells, cellsize,rulelive,ruledead)
        pygame.display.update()
alive=[]
dead=[]
rule='/234'#rules to set in format numer of neighbours required to live/to rebrith
rule=rule.split("/")
for i in rule[0]:
    alive.append(int(i))
for i in rule[1]:
    dead.append(int(i))
def randomrules(range):
    tab = np.random.randint(range, size=(np.random.randint(9, size=(1))))
    return tab

if __name__ == "__main__":
    while True:
            bul = True
            if(randomRules):
                alive = randomrules(9)
                dead = randomrules(9)
            main(100, 100, 5,alive,dead,bul)
            print(alive)
            print(dead)
            a = input("Aby wygenerować nową gre wpisz n, aby przerwać wpisz q\n")
            if(a=="n"):
                bul=False
