# # iterable = [1, 2, 3, 4]
# # elements = *iterable,
# # print(elements)
# # a, b, c = [*(1, 2, 3)]
# # print(a)
# # print(type(a))
#
#
# class Animal:
#     name = "AAA"
#
#     def __init__(self):
#         self.type = "Animal"  # 公有属性，可以被继承
#         self.__color = "__"  # 私有属性
#
#     def __move(self):
#         print("__move")
#
#
# class Cat(Animal):
#     # def __init__(self):
#     #     self.color = "black_cat"
#
#     def eat(self):
#         # print(self.__color)
#         print("C.eat")
#
#
# cat = Animal()
# cat1 = Cat()
# print(dir(cat))
# print(dir(cat1))
# print(cat.__dict__)
# print(cat1.__dict__)
# print(cat1.eat)
# # # cat.move()
# # try:
# #     cat1.eat()
# # except AttributeError as reason1:
# #     print(reason1)
# #
# # try:
# #     Animal.__move(cat1)
# # except AttributeError as reason2:
# #     print(reason2)
# #
# def func1():
#     try:
#         raise Exception
#     except:
#         return True
#     else:
#         return True
#     finally:
#         return False
#
# def main():
#     res = func1()
#     print(res)
#     print(type(res))
#
# if __name__ == "__main__":
#     main()


# 17.	编写一个在Python3解释器中运行的程序，输出一个九九乘法表（循环嵌套）。
# 参考代码：
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j),end="\t")
#     print()
# 18.	定义一个学生类，属性有姓名（name）、年龄（age）、性别（sex），方法有学习、休息，然后创建一个学生对象，调用学习和休息方法。
# 参考代码：
# class Student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def learn(self):
#         pass
#
#     def relax(self):
#         pass
#
#
# student1 = Student()
# student1.learn()
# student1.relax()

# 19.	定义一个函数main()，将1—200（范围包含1和200）中3的倍数或者有数字3的所有整数保存到列表list_1中，并输出。
# 参考代码：
#
#
# def main():
#     list1 = []
#     for i in range(1, 201):
#         if i % 3 == 0 or "3" in str(i):
#             list1.append(i)
#     print(list1)
#
#
# if __name__ == '__main__':
#     main()
#
# 20.	编写一个程序，输入文件名，并完成对文件的备份。
# 参考代码
# file_name = input("pls enter file name:")
# with open(file_name, "r") as file1:
#     context = file1.read()
#     with open(file_name + "_backup", "w") as file2:
#         file2.write(context)

# 21.	给定两个list ,A = [1,2,3,4,5,6,7,1,2,3]和B=[4,5,6,7,8,9,10,9,8,11]，请用python找出A,B 中相同的元素放入列表D中，找出A,B中不同的元素放入列表C中，确保C、D两个列表中的元素不重复（用代码实现）
# 参考代码：
# A = [1,2,3,4,5,6,7,1,2,3]
# B=[4,5,6,7,8,9,10,9,8,11]
# list_D = []
# list_C = list(set(A + B))
# for i in set(A):
#     if i in B:
#         list_D.append(i)
#         list_C.remove(i)
# print(list_C)
# print(list_D)

