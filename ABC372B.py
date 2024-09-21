z = int(input())
l = []
power = 0
while 3**power <= z:
    power += 1
for i in range(power-1,-1,-1):
    while 3**i <= z:
        l.append(i)
        z = z -3**i
print(len(l))
for i in range(len(l)):
    print(l[i],end=" ")