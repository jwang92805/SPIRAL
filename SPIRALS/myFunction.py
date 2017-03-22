def tear(t,size):
    #t.begin_fill()
    for times in range(10):
        t.width(10)
        c=(10,times*25,133)
        t.color(c)
        #print(c)
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
    #t.end_fill()
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t,distance):
    #t.color("blue")
    #polygon(t,5,distance)
    t.color("black")
    polygon(t,4,distance)
    t.color("orange")
    polygon(t,3,distance)

def coolsquared(t,distance):
    for times in range(4):
        cool(t,distance)
        t.right(90)

def jump(t,x,y):
    #t.penup()
    t.goto(x,y)
    #t.pendown()

def octoangle(t,distance):
    #t.begin_fill()
    for times in range(8):
        t.forward(distance)
        t.right(120)
        t.forward(distance)
        t.left(60)
    #t.end_fill()

def star(t,distance): 
    t.begin_fill()
    for times in range(4):
        t.forward(distance)
        t.left(60)
        t.forward(distance)
        t.right(150)
    t.end_fill()

def flower(t,size):
    for times in range(10):
        t.left(times*39)
        tear(t,size)
        t.penup()
        t.home()
        t.pendown()

def multistar(t):
    for times in range(20):
        octoangle(t,10)
        t.forward(10)
        t.left(36)
        t.forward(133)

def spiral(t):
    t.circle(100)
    t.left(35)
    
def multispiral(t):
    for times in range(155):
        c=(0,times,255-times)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(200,-200)
        c=(255-times,times,0)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(200,200)
        c=(times,255-times,0)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(-200,200)
        c=(0,255-times,times)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(-200,-200)
        c=(0,255-times,times)
        t.color(c)
        print(c)
        spiral(t)
        
    for times in range(155):
        t.goto(-200,0)
        c=(times,255-times,times)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(0,-200)
        c=(255-times,times,0)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(0,200)
        c=(0,times,255-times)
        t.color(c)
        print(c)
        spiral(t)

    for times in range(155):
        t.goto(200,0)
        c=(0,255-times,times)
        t.color(c)
        print(c)
        spiral(t)


def circles(t,sides):
    for times in range(sides):
        c=(0,times,255-times)
        t.color(c)
        print(c)
        t.circle(times*10)
        t.left(15)



    

