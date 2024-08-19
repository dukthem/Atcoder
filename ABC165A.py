k = int(input())
a, b = map(int, input().split())
c = 0
while a <= b:
    if (a % k == 0):
        c = c+1
    a += 1
if c > 0:
    print("OK")
else:
    print("NG")