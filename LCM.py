x , y = map(int,input().split())
for i in range(1,y+1):
    n = x*i
    if n%y==0:
        print(n)
        break