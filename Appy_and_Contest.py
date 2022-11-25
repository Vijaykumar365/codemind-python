def gcd(a,b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b,a%b)
for _ in range(int(input())):
    n,a,b,k= map(int,input().split())
    c=gcd(a,b)
    lcm=(a*b)//c 
    x=n//a+n//b-2*n//lcm
    if x>=k:
        print('Win')
    else:
        print('Lose')