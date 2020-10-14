from array import *
expenses = array('i', [])


n = int(input("Enter the number of expenses: "))
e = int(input("Enter the value of the first expense: "))
expenses.append(e)
sum = e

#24print(len(expenses))
for i in range (n-1):
    en = int(input("Enter the value of the next expense: "))
    expenses.append(en)
    sum += en
#print(expenses)
print(sum)