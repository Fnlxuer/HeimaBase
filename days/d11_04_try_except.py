"""try..except X..except..else..finally结构"""
try:
    print(a)
except BaseException as error:
    print("exist err: %s!" % error)
except NameError:
    print("name error")
except:
    print("exist error")
else:
    print("...")
finally:
    print("...")

"""try 嵌套或函数嵌套，异常传递给外层except语句进行处理"""
def func1():
    # 异常的基类是 BaseException
    # 推荐用 Exception，所有内置的，非系统退出的异常都源自这个类。所有用户定义的异常也应该从这个类派生
    raise Exception

try:
    try:
        func1()
    except IOError:
        print("IO err")
except:
    print("err")

"""自定义异常"""
class PhoneNumError(Exception):
    pass

try:
    phone_num = input("pls enter phone num:")
    if not phone_num.isdecimal():
        raise PhoneNumError("test")  #
except PhoneNumError as err:
    print("err: %s" % PhoneNumError)
