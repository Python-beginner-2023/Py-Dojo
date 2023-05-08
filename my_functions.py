
#!/usr/bin/python

def add(a, b):
    return a + b


x = add(3, 4)
print(f'x is : {x}')


def devide(a, b):
    q = a // b
    r = a % b

    return (q, r)


result = devide(7, 2)
print(f'result = {result}')

the_q, the_r = devide(15, 4)
print(f'q is {the_q}, and r is {the_r}')

the_q, _ = devide(19, 3)
print(f'q is {the_q}')


def max(a, b=0):
    if a > b:
        return a
    else:
        return b


print(f'max(3, 5) is {max(3, 5)}')
print(f'max(3, 5) is {max(3)}')

a = 100


def foo(x):
    a = x
    print(f'a ix {a}')


foo(3)
print(f'now a is :{a}')


def foo_2(x):
    global a
    a = x
    print(f'a ix {a}')


foo_2(30)
print(f'now a is :{a}')
