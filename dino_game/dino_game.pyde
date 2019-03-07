from collections import deque
from Dino import *
from Particle import *
    
POS_DINO = 100
myCar1 = Dino(POS_DINO, 300)
parts = deque(range(0,100))

def setup():
    size(800, 800)
    frameRate(30)
    
def draw():
    background(255)
    line(0, height/2 + 40, width, height/2 + 40)
    parts.append(Particle())
    parts.popleft()
    for el in parts:
        if not isinstance(el, int):
            if el.move():
                el.plot()
            else:
                del el
    myCar1.drive()
    myCar1.display()
    
def mouseClicked():
    myCar1.jump()
