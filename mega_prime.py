def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return 0
            break
    return 1
x = int(input())
if prime(x):
    n = str(x)
    m = len(n)
    c=0
    for i in n:
        if prime(int(i)):
            c+=1
    if c==m:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
    c=0
else:
    print('Not Mega Prime')