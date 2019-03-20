def setup():
    size(300, 300)
    background(255)
    strokeWeight(3)
    xo = 40
    yo = 200
    leng = int(random(50,100))
    i = 0
    points = []
    while( i < leng):
        i = i + int(random(13, 20))
        if(i > leng):
            points.append(leng)
        else:
            points.append(i)
    print(leng)
    print(points)
    ant = 0
    hant = 0
    for pnt in points:
        i = ant + 2
        j = hant
        desti = pnt - 2
        detj = h
        
        if pnt == leng:
            h = 0
        else:
            h = int(random(20, 45))
            line( xo + pnt - 2, yo -h, xo + pnt + 2, yo - h)
        ant = pnt
        hant = h
    line(xo, yo, xo+3, yo+3)
    line(xo+3, yo+3, xo + leng-3, yo+3)
    line(xo + leng -3, yo + 3, xo + leng, yo)
