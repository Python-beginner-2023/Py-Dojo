
#https://www.pinginglab.net/article/259
# 第2题

def add3(a, b, c):
    return a + b + c

x = add3(10, 20, 30)
print(x)

my_function = lambda a, b, c: a + b + c

y = my_function(30, 40, 50)
print(y)

#https://www.pinginglab.net/article/259
# 第3题

a = [1, 2, 3]
b = a
b[2] = 'hello'

print(a)
print(b)

import copy
a = [1, 2, 3]
b = copy.deepcopy(a)

b[2] = 'hello'

print(a)
print(b)


# https://www.pinginglab.net/article/259
# 7.

a = 10

b = 100 if a > 0 else -1
# b = 100 ? a>0 : -1