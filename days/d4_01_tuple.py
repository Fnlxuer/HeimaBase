# 元组不能增删（可以用 del 删除整个元组）改
# tuple_01 = (1, 2, 3)
"""仅包含单个数据的特殊性"""
# print(type(tuple_01))
# tuple_01 = 34
# print(tuple_01)
# print(type(tuple_01))
tuple_01 = ()
tuple_02 = ("12", [2,[3]])
tuple_03 = ("23",)*3
print(type(tuple_01))
print(tuple_03)
print(tuple_03 + tuple_02)
print(tuple_02[1:])
# 应用场景：元组是自动组包的默认类型、格式化字符的成分
# 内置函数：cmp()、len()、max()、min()、tuple()
# 运算符：* +(与extend的区别)
# 索引&截取：tuple_01[1]、tuple_01[-1]、tuple_01[0:]
# print("-"*30)
# tuple_04 = tuple(tuple_02)
# print(id(tuple_04),id(tuple_02))
# tuple_02[1].append(4)
# print(tuple_02,tuple_04,sep="\n")