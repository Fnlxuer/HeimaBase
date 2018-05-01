"""需求：
1、如果存在重复的键，user字典中的值应覆盖defaults字典中的值；
2、defaults和user中的键可以是任意合法的键；
3、defaults和user中的值可以是任意值；
4、在创建context字典时，defaults和user的元素不能出现变化；
5、更新context字典时，不能更改defaults或user字典。
"""
user = {'name': "Trey", 'website': "http://treyhunner.com"}
defaults = {'name': "Anonymous User", 'page_name': "Profile Page"}

# 1.字典拆分（Dictionary unpacking）in Python 3.5
# context = {**defaults, **user}

# 2.多次更新（multiple_update）
context = {}
context.update(defaults, **user)  # 注意 **kwargs 是由 **user 解包而来，user 的 key 必须符合规则（变量名命名）。
# context.update(defaults)
# context.update(user)

# # 3.复制，然后更新（copy and update）
# context = defaults.copy()
# context.update(user)
#
# # 4.字典解析（Dictionary comprehension）
# context = {k: v for d in [defaults, user] for k, v in d.items()}
#
# # 5.字典构造器（dict()）
# context = dict(defaults)
# context.update(user)

print(context)
