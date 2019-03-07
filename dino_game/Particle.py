class Particle(object):
    def __init__(self):
        self.ypos = 450 + random(300)
        self.xpos = width
        self.gusano = 0
        if random(100) <= 1:
            self.anim = 0
            self.gusano = 1
            
    def plot(self):
        if self.gusano == 1:
            if self.anim >= 0 and self.anim <= 5:
                img1 = loadImage("pixil-frame-0.png")
                image(img1, self.xpos, self.ypos);
            elif self.anim > 5:
                img1 = loadImage("pixil-frame-1.png")
                image(img1, self.xpos, self.ypos);
            elif self.anim >= -5 and self.anim < 0:
                img1 = loadImage("pixil-frame-2.png")
                image(img1, self.xpos, self.ypos);
            else:
                img1 = loadImage("pixil-frame-0.png")
                image(img1, self.xpos, self.ypos);
            self.anim += 3
            if self.anim > 10:
                self.anim = -10
        else:
            line(self.xpos, self.ypos, self.xpos + 10, self.ypos)
    
    def move(self):
        if self.xpos > 1:
            self.xpos = self.xpos - 14
            return True
        else:
            return False
