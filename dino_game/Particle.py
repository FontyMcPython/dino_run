class Particle(object):
    def __init__(self):
        self.ypos = 450 + random(300)
        self.xpos = width
        self.gusano = 0
        self.splat = 0
        if random(100) <= 1:
            self.anim = 0
            if random(10) > 5:
                self.gusano = 1
            else:
                self.gusano = 2
            
    def plot(self):
        if (self.gusano == 1 or self.gusano == 2) and self.splat == 0:
            if self.anim >= 0 and self.anim <= 5:
                if self.gusano == 1:
                    img1 = loadImage("pixil-frame-0.png")
                else:
                    img1 = loadImage("scorpi0.png")
                image(img1, self.xpos, self.ypos);
            elif self.anim > 5:
                if self.gusano == 1:
                    img1 = loadImage("pixil-frame-1.png")
                else:
                    img1 = loadImage("scorpi0.png")
                image(img1, self.xpos, self.ypos);
            elif self.anim >= -5 and self.anim < 0:
                if self.gusano == 1:
                    img1 = loadImage("pixil-frame-2.png")
                else:
                    img1 = loadImage("scorpi1.png")
                image(img1, self.xpos, self.ypos);
            else:
                if self.gusano == 1:
                    img1 = loadImage("pixil-frame-0.png")
                else:
                    img1 = loadImage("scorpi1.png")
                image(img1, self.xpos, self.ypos);
            self.anim += 3
            if self.anim > 10:
                self.anim = -10
        elif self.splat == 1:
            img = loadImage("splat.png")
            image(img, self.xpos, self.ypos)
        else:
            line(self.xpos, self.ypos, self.xpos + 10, self.ypos)
    
    def move(self):
        if self.xpos < 160 and self.ypos < 500 and self.gusano:
            self.splat = 1
        if self.xpos > 1:
            self.xpos = self.xpos - 14
            return True
        else:
            return False
        
