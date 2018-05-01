class Dog:
    type = "dog"

    def eat(self):
        print("eat dog's")


class God:
    def eat(self):
        print("eat god's")


class XTQ(Dog, God):
    pass


# xtq = XTQ()
# print(XTQ.__mro__)
# God.eat(xtq)
# super(XTQ, xtq).eat()

print(Dog.type)
Dog.type = "Happy Dog"
print(Dog.type)
