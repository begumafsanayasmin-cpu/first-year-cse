n=int(input("Enter a number of elements:"))
a=[]
for i in range(n):
    x=int(input("Enter element:"))
    a.append(x)
print("Original list:",a)

x=int(input("Enter element to insert:"))
pos=int(input("Enter index position:"))
a.insert(pos,x)
print("List after insertion:",a)


print("Enter element to delete:",a)
x = int(input())

a.remove(x)
print("List after deletion:", a)

print("List in ascending order:")
a.sort()
print(a)

a.reverse()
print("Reversed list:", a)

pos = a.index(x)
print("Index of the element is:", pos)

a.clear()
print("List after removing all elements:", a)