from collections import Counter
def first_recurring(a):
        b=Counter(a)
        for _ in a:
                if(b[_]!=1):
                        return _
input_string = input("Enter ")
userList = input_string.split()
print(first_recurring(userList))
