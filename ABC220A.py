a, b, c = map(int, input().split())
for i in range (a, b+1):
    i += a
    if a% c == 0:
        print(a)
        break
    elif a == b and b%c!=0:
        print(-1)
        break
    a += 1
