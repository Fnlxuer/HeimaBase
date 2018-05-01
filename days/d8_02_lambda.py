# 应用场景：sort 的 key 参数，key=函数名/匿名函数
def func_sort_1(x):
    return x["age"]


def func_sort_2(x):
    return x[1]


list1 = [{"name": "zs", "age": "18"}, {"name": "ls", "age": "81"}]
list1.sort(key=func_sort_1)
# list1.sort(key=lambda x: x["age"])
print(list1)

list2 = [[1, 5, 3], [2, 4, 8], [1, 1, 7]]
# list2.sort(key=lambda x: x[1])
list2.sort(key=func_sort_2)
print(list2)


