# # 思路一：将固定顺序的列表放入随机的几个列表中
# import random
# office_0 = []
# office_1 = []
# office_2 = []
# names = {"A", "B", "C", "D", "E", "F", "G", "H"}
# for name in names:
#     office_rand = "office_%s" % random.randint(0, 2)
#     s = locals()[office_rand]
#     s.append(name)

import random
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[] for i in range(3)]
for name in names:
    index_random = random.randint(0, 2)
    offices[index_random].append(name)
# 每个办公室人数和人员
i = 1
for office in offices:
    print("办公室%d的总人数是%d" % (i, len(office)), end=",名字分别为:")
    i += 1
    for name in office:
        print("%s" % name,end=" ")
    print()

