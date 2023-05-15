# https://zhuanlan.zhihu.com/p/54430650?utm_id=0

#1

list = range(1, 101)
c = 0
for i in list:
    c = c + i

x = sum(range(1, 101))

# 13

x = [1, 2, 3, 4, 5]
# b = map(lambda x: x*x, [1, 2, 3, 4, 5])
print(x)
y = [x for x in map(lambda x: x*x, [1, 2, 3, 4, 5])]
print(y)


# 14
import random

r = random.random()
x = (r * 5) + 15 # 15到20之间的随机数

#15

a_str = r"hello\n"
print(a_str)

# 17

a = 100
b = 20

assert a < b, "a应该要比b小"

c = b - a
print(c)