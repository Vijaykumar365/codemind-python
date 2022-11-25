def prime(i):
    if i==1:
        return 0
    for j in range(2,(i//2)+1):
        if j%i==0:
            return 0
    return 1
x = int(input())
c=0
for i in range(1,x):
    if x%i==0:
        if prime(i):
            print(i,end=" ")
            c+=1
if c==0:
    print('-1')