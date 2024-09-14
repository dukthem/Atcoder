n , m = list(map(int, input().split()))
s = set()
for i in range(m):
    cnt = 0
    c = list(s)
    a, b = list(map(str, input().split()))
    if b == "M":
        for j in range(len(s)):
            if a == c[j]:
                cnt += 1
        if cnt == 1:
            print("No")
        else:
            print("Yes")
            s.add(a)
    else:
        print("No")