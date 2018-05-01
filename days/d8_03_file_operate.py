# # file1 = open("abc.py", "w")
# # file1.write("OK?")
# # file1.close()
# #
# #
# import os
# path_name = os.getcwd()
# print(path_name)
# with open("abc.txt", "w", encoding="utf-8") as file2:
#     file2.write("1\n2\n3\t4\n")
#     # content_file2 = file2.read()
#     # print(content_file2)
#
# """路径写法
# 1.绝对路径
# 2.相对路径
# """
# """ 三种写法：
# r"...\..."
# "...\\..."
# ".../..."(推荐使用，大多数系统的写法)
# """
#
# with open("abc.txt", "r", encoding="utf-8") as file2:
#     read = file2.read()
#     read_n = file2.read(2)
#     readline = file2.readline()
#     readlines_list = file2.readlines()
#
# print(read, read_n, readline, readlines_list,sep="\n-----------------\n")
#
# open 方法 起名 数字开头
f_n = input("input file name:")
with open(f_n, "a+") as file1:
    file1.write("你好")
    print(file1.tell())
    # 设置光标定位，offset（设置偏移，当 whence 不为0时，offset 只能为0），whence 默认为0（0:开头，1:当前，2:结尾）
    file1.seek(1, 0)
    print(file1.tell())
    context = file1.read()
# 起名
# dot_index = f_n.rfind(".")
# n_f_n = f_n[:dot_index] + "_copy" + f_n[dot_index:]
# # copy
# with open(n_f_n, "a+") as file2:
#     file2.write(context)
#
# print(context)

