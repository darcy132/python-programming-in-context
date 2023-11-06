import random
import math

def isInCircle(point:list,radius):
    x,y=point
    if math.sqrt(x**2+y**2) <= radius:
        return True
    else:
        return False
a = [24,25]
print(isInCircle(a,40))

def montePi(numDarts):

    inCircle = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2+y**2)

        if distance <= 1:
            inCircle = inCircle + 1
    pi = inCircle / numDarts * 4
    return pi
print(montePi(100_000))
