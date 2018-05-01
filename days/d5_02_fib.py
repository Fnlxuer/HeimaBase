def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        list1 = [0, 1]
        for i in range(2, n):
            list1.append(list1[i-1]+list1[i-2])
        return list1


print(fib(7))
