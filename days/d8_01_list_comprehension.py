list1 = [i for i in range(3) for _ in range(3)]
print(list1)

list2 = []
for i in range(1,11):
    if i % 2 == 0:
        list2.append(i)
print(list2)

list3 = [i for i in range(1, 11) if i % 2 == 0]
print(list3)