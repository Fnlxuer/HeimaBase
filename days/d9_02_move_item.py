"""需求
打印 Item 时，显示 type、area
属性：type、area
方法：__str__
"""


class Item:
    def __init__(self, item_type, area):
        self.type = item_type
        self.area = area

    def __str__(self):
        return "Item's type is %s, area is %d" % (self.type, self.area)


item1 = Item("桌子", 81)
print(item1)

"""需求
class House
属性：address, area
方法：items(if free_area > item.area)
     __str__(address, area, free_area)
"""


class House:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.items = []

    def __str__(self):
        result_str = "add is %s, area is %d, free_area is %d, has items: " \
                     % (self.address, self.area, self.free_area)
        # 判断 items 数量，如 >0 则添加进 return 内容（去掉 ", "）
        if len(self.items) == 0:
            result_str += "None"
        else:
            for item in self.items:
                result_str += item.type + ", "
            result_str = result_str.strip(", ")
        return result_str

    def add_item(self, item):
        if self.free_area >= item.area:
            self.free_area -= item.area
            # save list of items
            self.items.append(item)
            print("added")
        else:
            print("ERR")


home = House("beijing", 80)
home.add_item(item1)
print(home)

