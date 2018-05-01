class Animal:
    def __init__(self, type, __color):
        self.type = type  # 公有属性，可以被继承
        self.__color = __color  # 私有属性，不可以被继承

    def eat(self):  # 公有方法，可以被继承
        print("A.eat")

    def __eat(self):  # 私有方法，不可以被继承
        print("__eat")


class Cat(Animal):
    def __init__(self, type, __color):
        self.type = "cat"
        super().__init__(type, __color)
        # self.__color = ("black", "white")

    def eat(self):
        print(self.__color)
        print("C.eat")

    def drink(self):
        print("drink")
        self.__eat()


class LittleCat(Cat):
    def eat(self):
        print("L.eat")

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        # 在类外面没法取得当前类名和对象名self
        super().eat()
        return self.__name
    pass


# cat1 = LittleCat("Kitty")
# print(cat1)
# # 调用被重写的父类方法
# Animal.eat(cat1)
# super(LittleCat, cat1).eat()
cat_cat = Cat("bosi", "yellow")
print(cat_cat.type)
cat_cat.eat()
