s = input()
a = 0
for i in range(0, 2):
    if s[i] == s[i+1]:
        a += 1
if a == 2:
    print("Won")
else:
    print("Lost")