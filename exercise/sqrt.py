import math
def sqrt(num,acc):
    x = 1
    for i in range(acc):
        x = (x + num*x)/2
    return x
print(sqrt(2,1000),math.sqrt(2))