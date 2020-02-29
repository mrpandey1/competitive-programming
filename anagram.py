a='mmmm'
b='maam'
def ana(a,b):
    i=0
    while a[i] in b:
        i=i+1
    return len(b)==i
print(ana(a,b)
from collections import Counter
def fund(a,b):
    return Counter(a)==Counter(b)
a=input("enter word")
b=input("enter word")
print(fund(a,b))
