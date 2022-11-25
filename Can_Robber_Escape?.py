r=int(input())
l=0
v=list(map(int,input().split()))
for k in range(0,len(v)):
    if v[k]%2!=0:
        l+=1
if l<=2:
    print('YES')
else:
    print('NO')