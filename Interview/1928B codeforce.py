def solution():
    n = int(input())
    lis = list(map(int,input().split()))
    s = set(lis)
    ss = sorted(s)
    mx = 0
    f = 0
    for i in range(len(ss)):
        while f < len(ss) and ss[f]<ss[i]+n:
            f+=1
        mx = max(f-i,mx)
    print(mx)
for _ in range(int(input())):
    solution()