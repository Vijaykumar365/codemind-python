v,k=map(int,input().split())
l=v+2*k
if v==0 and k%2==0:
    print('YES')
elif v==0 and k%2!=0:
    print('NO')
elif l%2==0:
    print('YES')
else:
    print('NO')