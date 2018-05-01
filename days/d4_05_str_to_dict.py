"""k:1|k1:2|k2:3|k3:4"""
# 思路一：dict()
s = "k:1|k1:2|k2:3|k3:4"
l1 = s.split("|")
l2 = []
for i in l1:
    l2.append(tuple(i.split(":")))
d = dict(l2)
print(d)

s.replace(":","")

# 思路二：for循环定义 dict[key] = value
s = "k:1|k1:2|k2:3|k3:4"
l1 = s.split("|")
d = {}
for i in l1:
    l2 = i.split(":")
    d[l2[0]] = l2[1]
print(d)

# 思路三：update
s = "k:1|k1:2|k2:3|k3:4"
l1 = s.split("|")
d = {}
for i in l1:
    t_temp = tuple(i.split(":"))
    d.update((t_temp,))
print(d)