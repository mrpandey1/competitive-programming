def maximumToys(prices, k):
    prices.sort()
    sum=0
    count=0
    for _ in prices:
        if(sum+_>k):
            return count
        sum+=_
        count+=1
    return count
nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
result = maximumToys(prices, k)
print(result)
