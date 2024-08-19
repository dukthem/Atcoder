s = input()
test = ""
test2 =""
for i in range(len(s)-1, -1, -1):
    if s[i] != ".":
        test += s[i]
    else:
        break
for i in range(len(test)-1, -1, -1):
    test2 += test[i]
print(test2)