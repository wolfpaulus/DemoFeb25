"""
 I'd like to approximate pi using the monte carlo method and python's random number generator.
"""
import math
import random


k = 0
n = 0
approx = 0;
while abs(approx - math.pi) < ...:  # todo until the approx is good enough.
    n += 1
    x, y = random.random(), random.random()
    # is the coordinate (x,y) inside the circle or not?

    if (x * x + y * y) <= 1:  # yes it's inside.
        k += 1

    approx = 4 * k / n

print("..." + str(n))
print("that's it")