n , m , k = map(int, input().split())
a = []
b = [n , m]
b.sort()
while len(a) != k+1:
    i = 1
    if (i % n != 0 and i % m == 0) or (i % n == 0 and i % m != 0):
        a.append(i)
        a.sort()
        print(a)
    i += 1    
print(a[k-1])
            