import random
import matplotlib.pyplot as pyplot
from decimal import Decimal

pyplot.ion()

maxPoints = 2000
maxIteration = 1000

a = 1.4
b = 0.3

def henon(p):
    x = Decimal(p[0])
    y = p[1]
    x1 = Decimal(1) - Decimal(a)*pow(x, Decimal(2)) + Decimal(y)   
    y1 = Decimal(b) * x
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


def iteration():
    pyplot.title("Henon map with "+str(maxPoints) + " points with a=" + str(a) + " b=" + str(b))

    xpoints, ypoints, colors = makePoints()

    pyplot.scatter(xpoints, ypoints, marker='.', c=colors)
    pyplot.pause(0.01)
    pyplot.clf()


if __name__ == '__main__':
    for i in range(maxIteration):
        print(i, a, b)
        try:
            iteration()
        except:
            print("Decimal overflow reached.")
            a = 1.4
            b = 0.3
            iteration()

        a = a - 0.01
        b = b - 0.01
    






            

