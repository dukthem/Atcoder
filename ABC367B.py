x = input()
for i in range(len(x)-1, -1, -1):
    if x[i] == "0":
        x = x[:i]
    else:
        if x[i] == ".":
            x = x[:i]
            break
        else:
            break
print(x)