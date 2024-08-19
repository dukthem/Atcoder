C = input()
sum = "abcdefghijklmnopqrstuvwxyz"
a = 0
if C != "z":
    for i in range(0, len(sum)):
        if (C == sum[i]):
            print(sum[i+1])
        i += 1