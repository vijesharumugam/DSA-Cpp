N = int(input())
interval = []
for _ in range(N):
    interval.append(list(map(int,input().split())))



interval.sort()
start = interval[0][0]
while(start<=end):
    d = (start+end)//2
    path = interval[0][0]

    i = 1
    while i < N:
        f = (path+d)
        if f >interval[i][1]:
            end = d-1
            break
        else:
            path = max(f,interval[i][0])
        i+=1
    if i == N:
        ans = d
        start = d+1
print(ans)