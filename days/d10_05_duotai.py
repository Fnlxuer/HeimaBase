"""多态：同类对象的不同表现形式（子类化）
继承-重写-调用继承父类的方法"""

class People:
    def dance(self):
        print("dance")

    def play(self):
        self.dance()

class OldMan(People):
    def dance(self):
        print("g_dance")

class YoungMan(People):
    def dance(self):
        print("street_dance")


xiaoming = YoungMan()
laowang = OldMan()
xiaoming.play()
laowang.play()
