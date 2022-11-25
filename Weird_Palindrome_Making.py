for _ in range(int(input())):
    _=int(input())
    v=list(map(int,input().split()))
    k=0
    for r in v:
        k+=(r%2)
    print(k//2)