from linked_list import LinkedList

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
lst.append(6)

lst.prepend(0)
print(lst)
print(len(lst))

lst.insert(3, -1)
print(lst)

lst.delete_by_value(4)
print(lst)

lst.delete_by_value(6)
print(lst)

lst.delete_by_value(0)
print(lst)

print(len(lst))
