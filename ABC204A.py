x = list(map(int, input().split()))
i = 0
x_sort = sorted(x)
if x[0] == x[1]:
    print(x[0])
else:
    if x_sort[0] == 1:
        print(0)
    else:
        if x_sort[1] == 1:
            print(2)
        else:
            print(1)