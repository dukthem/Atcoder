a, b, c = map(int, input().split())
if c - b > 0:
    if a < b or c < a:
        print("Yes")
    else:
        print("No")
else:
    if a < b and a > c:
        print("Yes")
    else:
        print("No")
