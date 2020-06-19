import random
import matplotlib.pyplot as pyplot

maxPoints = 20000

a = 1.4
b = 0.3

def henon(p):
    x = p[0]
    y = p[1]
    x1 = 1 - a*pow(x, 2) + y
    y1 = b * x
    return x1, y1

def makePoints():
    xpoints = []
    ypoints = []
    colors = []

    pos = [0, 0]

    for i in range(maxPoints):
        xpoints.append(pos[0])
        ypoints.append(pos[1])
        colors.append(i)

        pos = henon(pos)
        
    return xpoints, ypoints, colors

    
if __name__ == '__main__':
    xpoints, ypoints, colors = makePoints()

    pyplot.scatter(xpoints, ypoints, marker='.', c=colors)

    pyplot.title("Henon map with "+str(maxPoints) + " points")
    pyplot.show()
            

