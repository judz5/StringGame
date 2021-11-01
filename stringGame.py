import pygame

pygame.init()
win = pygame.display.set_mode([500,700])

prevLine = [[(250,650), (250,650)]]

strings = []

previous_point = (250,650)
cameraShift = 0

#colors
class color():

    black = (0,0,0) # normal string
    navy = (20,33,61) # maybe some kind of special string
    orange = (252, 163, 17) # ball
    grey = (229, 229, 229) # background 
    white = (255,255,255)

# class string:
#     def __init__(self, event):
#         self.x1 = event.pos[0]
#         self.y1 = None
#         self.x2 = None
#         self.y2 = None

#     def setStart(self, pos):
#         self.x1 = pos[0]
#         self.y1 = pos[1]

#     def setEnd(self, pos):
#         self.x2 = pos[0]
#         self.y2 = pos[1]

#     def drawString(self, cameraShift):
#         if self.x2 != None and self.y2 != None:
#             pygame.draw.line(win, color.black, (self.x1, self.y1 + cameraShift), (self.x2, self.y2 + cameraShift), 10)
#         else:
#             self.x2 = self.x1
#             self.y2 = self.y1              

def addLine(event, cameraShift):
    global previous_point

    x = event.pos[0]
    y = event.pos[1] + cameraShift
    
    if previous_point != None:
        prevLine.append([previous_point, (x,y)])
        previous_point = None
    previous_point = (x,y)
    
def drawAll(cameraShift):
    for i in range(len(prevLine)):
        first = prevLine[i][0]
        last = prevLine[i][1]
        pygame.draw.line(win, color.black, (first[0], first[1]), (last[0], last[1] + cameraShift), 10)
       

def reset():
    global prevLine, previous_point
    prevLine.clear()
    prevLine.append([(250,650), (250,650)])
    previous_point = (250,650)
    win.fill((255,255,255))

class Ball:
    def __init__(self):
        self.x = 250
        self.y = 350
        self.dx = 0
        self.dy = 0
        self.gravity = 0.3

    def setY(self, y):
        self.y = y

    def setX(self, x):
        self.x = x

    def drawBall(self,cameraShift):
        pygame.draw.circle(win, color.orange, (self.x, self.y+cameraShift), 20)

def main():
    run = True
    ball = Ball()
    clock = pygame.time.Clock()
    cameraShift = 0
    while run:
        clock.tick(60)

        ball.dy += ball.gravity
        ball.setY(ball.y + ball.dy)

        if ball.y > 680:
            ball.dy *= -1.1

        if ball.y < 350:
            cameraShift = -ball.y + win.get_height()/2 - 20
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                addLine(event, cameraShift)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset()
        pygame.display.update()
        win.fill(color.grey)
        drawAll(cameraShift)
        ball.drawBall(cameraShift)
    pygame.quit()


main()