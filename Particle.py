class Particle(object):
    def __init__(self):
        self.ypos = 450 + random(300)
        self.xpos = width
        
    def plot(self):
        line(self.xpos, self.ypos, self.xpos + 10, self.ypos)
    
    def move(self):
        if self.xpos > 1:
            self.xpos = self.xpos - 14
            return True
        else:
            return False