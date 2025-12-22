n,k = map(int,input().split())
s = input()
ds = sorted(set(s))
if k<=n:
    t = s[:k]
    t = list(t)
    for i in range(k-1,-1,-1):
        ind = ds.index(t[i])
        if ind+1<len(ds):
            t[i] = ds[ind+1]
            break
        else:
            t[i]=ds[0]
    t= "".join(t)
else:
    t = s + (ds[0]*(k-n))
print(t)
