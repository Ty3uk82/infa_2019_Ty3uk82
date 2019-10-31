from graph import *
windowSize(800, 400)

def draw_sky():
    penColor(0, 255, 255)
    penSize(5)
    brushColor(0, 255, 255)
    rectangle(0, 0, 800, 180)

def draw_sea():
    penColor("blue")
    penSize(5)
    brushColor("blue")
    rectangle(0, 180, 800, 280)

def draw_sand():
    penColor("orange")
    penSize(5)
    brushColor("orange")
    rectangle(0, 280, 800, 400)

def draw_cloud(x, y, size):
    r = size
    x2 = x - r
    y2 = y +  r
    penColor(176, 196, 222)
    penSize(1)
    brushColor("white")

    for i in range(3):
        circle(x, y, r)
        x += r

    for i in range(4):
        circle(x2, y2, r)
        x2 += r


def draw_sun(x, y, size):
    penColor("yellow")
    penSize(1)
    brushColor("yellow")
    circle(x, y, size)

def draw_a_boat(x, y, size):
    def draw_sail():
        vertex1  = (100, 200)
        vertex2 = (130, 200)
        vertex3 = (90, 250)
        vertex4 = (90, 150)
        vertex7 = (-3, 0)
        vertex5 = (vertex4[0]+vertex7[0],vertex4[1] )
        vertex6 = (vertex3[0]+vertex7[0],vertex3[1] )


        triangle1 = [vertex1, vertex2, vertex3]
        triangle2 = [vertex1, vertex2, vertex4]
        mast = [vertex4, vertex5, vertex6, vertex3]
        print(mast)
        print(vertex5)
        print(vertex6)



        penColor("black")
        penSize(1)
        brushColor(255, 239, 213)

        polygon(triangle1)
        polygon(triangle2)

        penColor("black")
        brushColor("black")
        polygon(mast)



        pass
    draw_sail()
    pass

def draw_an_umbrella(x, y, size):
    pass



draw_sky()
draw_sea()
draw_sand()
draw_cloud(80, 80, 9)
draw_cloud(340, 90, 14)
draw_sun(450, 60, 30)

draw_a_boat(1, 1, 1)
draw_an_umbrella(1, 1, 1)



run()