def palin(n):
    n = str(n)
    m = n[::-1]
    if m==n:
        return 1
    return 0
a = int(input())
for i in range(a-1,0,-1):
    if palin(i):
        n = i
        break
j = a+1
while True:
    if palin(j):
        m = j
        break
    j+=1
if (a-n)==(m-a):
    print(n,end=" ")
    print(m)
elif (a-n)<(m-a):
    print(n)
else:
    print(m)