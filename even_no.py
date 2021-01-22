mylist = [int(i) for i in input("Enter the elements ").split()]
even =[]
for i in mylist:
    if i%2==0:
        even.append(i)
print(even)