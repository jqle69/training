def func(a, b=[]):
    b.append(a)
    return b

x=func(1)
y=func(2)
print(y)
