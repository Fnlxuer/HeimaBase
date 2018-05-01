"""创建对象时，自动调用__new__（必须有return（object.__new__(cls)（类似调用父类方法））、静态方法(显然，调用方法时实例未创建)）；
return new_object
创建完成后，自动调用__init__方法"""

class Dog:
    def __new__(cls, *args, **kwargs):
        # return object.__new__(cls)
        return 123

dog1 = Dog()
print(dog1)
