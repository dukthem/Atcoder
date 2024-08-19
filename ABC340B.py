q = int(input())
A = []
B = []
for i in range(0, q):
    a , b = map(int, input().split())
    if a == 1:
        A.append(b)
        B.insert(0, b)
        
    
    else:
        #for j in range(1, len(A)):
        #    B.append(A[len(A)-j])
        print(B[b-1])
        #B.clear()