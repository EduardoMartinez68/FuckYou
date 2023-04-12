import pygame, sys
pygame.init()
size=1000,600
sizeCube=25
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Fuck You level editor")
level=[]
baldosaX=0
baldosaY=0
mouseX,mouseY=0,0

def drawLine(x,y,x2,y2):
    index=12
    pygame.draw.line(screen,(index,index,index),[x,y],[x2,y2],1)

def updateScreen():
    screen.fill((0,0,0))
    for y in range(int(size[1]/sizeCube)):
        y=y*sizeCube
        drawLine(0,y,size[0],y)

    for x in range(int(size[0]/sizeCube)):
        x=x*sizeCube
        drawLine(x,0,x,size[1])      

    #draw position mouse 
    x,y=int(mouseX/sizeCube)*sizeCube,int(mouseY/sizeCube)*sizeCube
    pygame.draw.rect(screen,(255,255,255),[x,y,sizeCube,sizeCube],1)


    pygame.display.flip() 


def createArrayMap():
    for y in range(int(size[1]/sizeCube)): 
        wall=[]
        for x in range(int(size[0]/sizeCube)):
            wall.append(0)
        level.append(wall)
createArrayMap() 



while True:
    for event in pygame.event.get():
        mouseX,mouseY=pygame.mouse.get_pos()
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==45:
                sizeCube-=25
            elif event.key==61:
                sizeCube+=25
            sizeCube=25 if sizeCube<=0 else sizeCube

        if event.type==pygame.MOUSEBUTTONDOWN:
            baldosaX,baldosaY=int(mouseX/sizeCube),int(mouseY/sizeCube)
        
    updateScreen()

