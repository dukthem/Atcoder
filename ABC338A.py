cnt = 0
s = input()
if ord(s[0]) < ord("a"):
    for i in range(1, len(s)):
        if ord(s[i]) > ord("Z"):
            cnt += 1
    if cnt == len(s) -1:
        print("Yes")
    else:
        print("No")
else:
    print("No")