# 大驼峰命名类名
class NoteBook:
    def __init__(self, pages, name="notebook"):  # 带 "__" 的方法会由系统自动调用
        """创建对象时自动调用此方法，可以在此设定对象的统一属性（类通用）"""
        self.name = name
        self.pages = pages

    def __str__(self):
        """print 对象时，打印返回值（必须为 str）"""
        return self.name

    # @staticmethod
    def open(self):
        print("%s has been opened, pages is %d" % (self.name, self.pages))


# 创建相应对象、设定属性及调用方法
notebook1 = NoteBook(pages=1, name="Xuer's notebook")
notebook2 = NoteBook(2)
# notebook1.name = "Xuer's notebook"
# notebook2.name = "My notebook"
notebook1.open()
notebook2.open()
print(notebook1)
