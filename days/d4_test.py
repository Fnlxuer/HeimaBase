# 关卡一：
# 1、写出 for 循环的完整格式，并简单描述 for 循环的执行过程
# for 元素 in 序列:
#     循环体
# 执行过程为遍历序列中的每一个元素，执行循环体中的代码。
# 2、使用 for 循环遍历字符串 "ILoveYou"，当字符串为 "e" 的时候终止循环。
# for letter in "ILoveYou":
#     if letter == "e":
#         break
# 3、python 中定义字符串的四种方式
# ""
# ''
# """"""
# ''''''
# 4、有字符串a="abcdef",怎么使用下标来获取字符串中的字符"c"
# a="abcdef"
# b = a[2]
# print(b)
# 5、怎样测得字符的长度
# len(str)
# 6、列表嵌套的格式
# [[], [], ..., []]
# 7、向字典 info字典中添加新的键值对，保存如下信息：姓名是张三
# info["姓名"] = "张三"
#
# 关卡二：
#
# 1、使用列表嵌套，完成8名老师随机分配3个办公室
import random
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[]] * 3
print(offices[0])
for teacher in teachers:
    index_random = random.randint(0, 2)
    offices[index_random].append(teacher)
print(offices)
# 2、从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母
# 3、使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自 键盘的输入
#
#
# 关卡三：
# 1、统计字符串中，各个字符的个数
#
# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1