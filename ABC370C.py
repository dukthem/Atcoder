s = input()
t = input()
y = []
z = []
x = []
cnt = 0
for i in range(len(s)):
    z.append(t[i])
    y.append(s[i])
# while y != z:
#     for i in range(len(s)):
#         if y[i] != z[i]:
#             y[i] = z[i]
#             cnt += 1
#         x.append(y)
#         print(x)
while y != z:
    for i in range(len(s)):
        if y[i] != z[i]:
            y[i] = z[i]
            cnt += 1
            x.append(y)
            print(x)
        elif y[i] == z[i]:
            continue
print(cnt)
# for i in range(len(x)):
#     for j in range(len(y)):
#         print(x[i][j], end="")
#     print('')