# # hi = 100
# # route = 100
# # for i in range(1,11):
# #     hi /= 2
# #     route = route + hi*2
# #     if i == 9:
# #         route_end = route
# #
# # print(route_end)
# # print(hi)
#
#
# # a = "1", "2"
# # *d, = a
# # *a, = *d,
# # print(d,a)
# # print(type(d), type(a))
# # seq = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# # for a, b, c in seq:
# #     print(a, b, c)
# #
# # *a, *b = range(1, 5, 1)
# # print(a, b)
#
# (a, b), (c, d, e, f) = [1, 2], 'this'
# print(a, b, c)
# print(type(a), type(c))
#
# # for  in range(1,5):
# #     i*(i-1)
#
#
# def step_1(n):
#     if n == 0:
#         return 0
#     else:
#         return n + step_1(n-1)
#
#
# def step_2(n):
#     print(n)
#     step_2(n+1)
#
#
# print(step_1(5))
# print(step_2(1))

#
# class Animal:
#     type = "A"
#
#     @classmethod
#     def cls_test(cls):
#         print("test")
#
#
# class Dog(Animal):
#     pass
#
#
# dog1 = Dog()
# Animal.cell = "animal's cell"
# print(dog1.type)
# print(dog1.cell)
# dog1.cls_test()


class Teacher(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 说话
    def talk(self):
        print('%s 说：你们是女生最少的一个班')
    # 大哭
    def cry(self):
        print('%s 说: 我都 %d 岁了，连一个亿都没挣到')


xm = Teacher('小明',20)
print('%s 的年龄是 %d' % (xm.name, xm.age))
xh = Teacher('小红', 19)
