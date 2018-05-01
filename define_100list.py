# i: shallow copy
# offices = [[] for i in range(100)]
# print(offices)

# ii:
i = 1
while i <= 100:
    name_str = "office_%s" % i
    s = locals()[name_str]
    s = []
    print(s)
    i += 1
