def ans(a,b,c):
    t1=a[0:b]
    print(t1)
    t2=a[c+1:]
    print(t2)
    a=sorted(a[b:c+1],reverse=True)
    print(a)
    return t1+''.join(a)+t2
print(ans('effort',1,4))
