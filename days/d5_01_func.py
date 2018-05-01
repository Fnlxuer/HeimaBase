# 检测对象是否 iterable
def isiterable(p_object):
    try:
        it = iter(p_object)
    except TypeError:
        return False
    return True


print(isiterable(1))
