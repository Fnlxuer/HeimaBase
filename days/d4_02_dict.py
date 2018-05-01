"""整理列表，归类得到字典
    {
    'plant': ['cactus'],
    'animal': ['bear', 'duck'],
    'vehicle': ['speed boat', 'school bus']
    }
    """
data = [
    ("animal", "bear"),
    ("animal", "duck"),
    ("plant", "cactus"),
    ("vehicle", "speed boat"),
    ("vehicle", "school bus")
    ]
groups = {}
# for key,value in data:
#     if key in groups:
#         groups[key].append(value)
#     else:
#         groups[key] = [value]
for key, value in data:
    groups.setdefault(key, []).append(value)
print(groups)

"""实现 switch ... case 语句
if arg == 0:
    return 'zero'
elif arg == 1:
    return 'one'
elif arg == 2:
    return "two"
else:
    return "nothing"
"""
# data = {
#     0:"zero",
#     1:"one",
#     2:"two"
# }
# data.get(arg, "nothing")
