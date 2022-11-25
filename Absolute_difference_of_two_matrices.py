a=int(input())
m=[]
n=[]
s=0
l=[]
for i in range(a):
    u=list(map(int,input().split()))
    m.append(u)
for i in range(a):
    v=list(map(int,input().split()))
    n.append(v)
for i in range(a):
    p=[]
    for j in range(a):
        s=m[i][j]-n[i][j]
        p.append(abs(s))
    l.append(p)
for i in l:
    print(*i)