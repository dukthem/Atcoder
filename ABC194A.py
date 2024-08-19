x , y = map(int, input().split())
a = 0
b = 0
c = 0
d = x+y
if d>=15 and y >= 8:
    print(1)
    a = 1
elif d>= 10 and y >= 3:
    print(2)
    b = 1
elif d >= 3 and a == 0 and b == 0:
    print(3)
else:
    print(4)