class ShoppingCart:
    # 类属性，记录创建与否（创建前后值发生变化）、记录所创建的对象供返回
    new_object = None

    def __new__(cls, *args, **kwargs):
        # 判断创建与否
        if cls.new_object is None:
            cls.new_object = object.__new__(cls)
        return cls.new_object

    # def __new__(cls, *args, **kwargs):
    #     """改用hasattr方法（属性为str），少设置初始值"""
    #     if not hasattr(cls, "has_instance"):
    #         cls.has_instance = object.__new__(cls)
    #     return cls.has_instance


ShoppingCart.new_object = 1
sc1 = ShoppingCart()
print(sc1)
