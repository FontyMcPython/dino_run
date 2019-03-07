gravedad = 3
class Dino(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.yspeed = 0
        self.anim = 0
        self.img1 = loadImage("dinorun0000.png")
        
    
    def display(self):
        if self.anim >= 0:
            img1 = loadImage("dinorun0000.png")
            image(img1, self.xpos, self.ypos);
        else:
            img2 = loadImage("dinorun0001.png")
            image(img2, self.xpos, self.ypos);
        self.anim += 1
        if self.anim >= 5:
            self.anim = -5
        
    def drive(self):
        self.ypos = self.ypos - self.yspeed;
        if self.ypos > height/2 :
            self.ypos = height/2
            self.yspeed = 0
        if self.ypos < height/2:
            self.ypos = self.ypos - self.yspeed;
            self.yspeed = self.yspeed - gravedad
    def jump(self):
        if self.ypos == height/2:
            self.yspeed = 30
            self.ypos = height/2 - 1
