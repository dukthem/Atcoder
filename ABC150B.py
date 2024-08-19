x = int(input())
y = input()
cnt = 0
for i in range(0, len(y) - 2):
    if y[i : i + 3] == "ABC":
        cnt += 1
print(cnt)