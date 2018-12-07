import csv
import pygame
from pygame.locals import *
import sys
import copy

class Cell:
    def __init__(self,state,nb):
        self.state = state
        self.nb = nb
    
    
def initCell():
    f = open("celldata.csv")
    data = csv.reader(f)
    for row in data:
        r = [Cell(int(i),0) for i in row]
        cells.append(r)

def nextGeneration():
    global cells
    temp = copy.deepcopy(cells)
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j].nb = 0
            
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            for x in range(9):
                if moves[x][0] == 0 and moves[x][1] == 0:
                        pass    
                else:
                    try:
                        if temp[i + moves[x][0]][j + moves[x][1]].state == 1:
                            temp[i][j].nb += 1
                    except:
                        pass
                    
    cells = copy.deepcopy(temp)

def lifeGamePlay():
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode((width,height))
    screen.fill(WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                nextGeneration()
                for i in range(len(cells)):
                    for j in range(len(cells[0])):
                        if cells[i][j].state == 0:
                            if cells[i][j].nb == 3:
                                cells[i][j].state = 1
                        else:
                            if not(cells[i][j].nb == 2 or cells[i][j].nb == 3):
                                cells[i][j].state = 0
                    
        
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                if cells[i][j].state:
                    pygame.draw.rect(screen,RED,(j*width/5,i*height/5,width/5-1,height/5-1))
                else:
                    pygame.draw.rect(screen,GRAY,(j*width/5,i*height/5,width/5-1,height/5-1))
        pygame.display.flip()



cells = []
initCell()
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (125,125,125)

moves = [[-1,-1],[0,-1],[+1,-1],
         [-1,0], [0,0], [+1,0],
         [-1,+1,],[0,+1],[+1,+1]]

lifeGamePlay()

