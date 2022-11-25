def prm(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
v=int(input())
k=int(input())
c=0
for _ in range(v,k+1):
    if prm(_):
        c+=1
print(c)