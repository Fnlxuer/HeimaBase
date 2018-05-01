# 不打印一行
import keyword
print(keyword.kwlist)
a = None
a1 = None,'None'
def ll(a):
    i = 1
    while i <= a:
        j = 1
        while j <= i:
            # if i == 3:
            #     # j += 1
            #     # continue
            #     break
            print("%d*%d=%-4d" % (j, i, i*j),end="\t")
            j += 1
        print()
        i += 1
ll(3)

# # 不打印一列
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         if j == 3:
#             # 无法使用Break删除某一列,因为此99表生成办法是逐行生成,在某一列打断会导致此行后面不能生成
#             j += 1
#             continue
#         print("%d*%d=%d" % (j, i, i*j),end="\t")
#         j += 1
#     print()
#     i += 1
#
# # 换个生成办法:一列一列生成
# 因为Print的机制,无法一列一列生成99表
