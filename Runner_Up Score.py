list_item = []
number = int(input("Enter number of elements : "))
for i in range(0, number):
    element = int(input())
    list_item.append(element)  # adding the element
mylist = list(dict.fromkeys(list_item))#converting to dictionary bcz dictionary does not contain any duplicates key.
mylist.sort()
mylist.pop()
print(max(mylist))

