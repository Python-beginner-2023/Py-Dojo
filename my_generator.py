
def N(limit):
    n = 1
    while n < limit:
        yield n
        n = n + 1

my_n = N(500)

for i in range(10):
    value = next(my_n)
    print(f'value is {value}')

ran = range(10)
ran = list(ran)
print(f'range is {ran}')