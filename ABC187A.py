a, b = map(str, input().split())
c = 0
d = 0
for i in range(0, 3):
    c += int(a[i])
for f in range(0, 3):
    d += int(b[f])
print(max(c, d))