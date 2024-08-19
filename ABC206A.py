x = int(input())
a = x* 1.08
import math
if  math.floor(a) < 206:
    print("Yay!")
elif math.floor(a) == 206:
    print("so-so")
else:
    print(":(")