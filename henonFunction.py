import random
import matplotlib.pyplot as pyplot

maxPoints = 20000

defaultA = 1.4
defaultB = 0.3

def henon(p, a, b):
    x = p[0]
    y = p[1]
    x1 = 1 - a*pow(x, 2) + y
    y1 = b * x
    return x1, y1

def makePoints(a, b):
    xpoints = []
    ypoints = []
    colors = []

    pos = [0, 0]

    for i in range(maxPoints):
        xpoints.append(pos[0])
        ypoints.append(pos[1])
        colors.append(i)

        pos = henon(pos, a, b)
        
    return xpoints, ypoints, colors

def graph(a, b):
    xpoints, ypoints, colors = makePoints(a, b)

    pyplot.scatter(xpoints, ypoints, marker='.', c=colors)

    pyplot.title("Henon map with "+str(maxPoints) + " points")
    pyplot.show()
    
if __name__ == '__main__':
    aIn = input("Value A for graph ('default' for 1.4): ")
    bIn = input("Value B for graph ('default' for 0.3): ")

    if aIn == 'default':
        a = defaultA
    else:
        a = float(aIn)

    if bIn == 'default':
        b = defaultB
    else:
        b = float(bIn)
    
    xpoints, ypoints, colors = makePoints(a, b)

    pyplot.scatter(xpoints, ypoints, marker='.', c=colors)

    pyplot.title("Henon map with "+str(maxPoints) + " points")
    pyplot.show()
            

