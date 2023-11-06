import math
def edulidD(point1,point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index])**2
        total += diff
        
    edulidDistance = math.sqrt(total)
    return edulidDistance