from collections import Counter
n, r = map(int, input().split())
arr = list(map(int, input().split()))
a1=Counter()
a2=Counter()
count=0
arr.reverse()
for i in arr:
    if i*r in a2:
        count+= a2[i*r]
    if i*r in a1:
        a2[i]+=a1[i*r]
    a1[i]+=1
print(count)
