x= int(input())
a = 0
if x % 100 != 0:
    while x % 100 != 0:
        x += 1
        a += 1
    print(a)
else:
    print(100)