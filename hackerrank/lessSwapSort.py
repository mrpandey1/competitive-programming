def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def countSwaps(a):
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=swap(a[j],a[j+1])
                count+=1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
n = int(input())
a = list(map(int, input().rstrip().split()))
countSwaps(a)
