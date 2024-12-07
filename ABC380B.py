s = input()
s = s[1:]
cnt = 0
for i in range(len(s)):
    if s[i] == "|":
        print(cnt, end=" ")
        cnt = 0
        continue
    else:
        cnt += 1