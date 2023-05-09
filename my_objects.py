
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_cn = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']


class MyStack():

    @staticmethod
    def version():
        return '1.0.0'

    def __init__(self) -> None:
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def length(self):
        return len(self._data)


s = MyStack()
s2 = MyStack()
s3 = MyStack()

s.push(1)
s.push(2)
s.push(3)

print(f'length is {s.length()} after push 3 items')

print(s.pop())
print(s.pop())
print(s.pop())

print(f'length is {s.length()} after pop 3 items')


class MyClass2(list):

    def push(self, item):
        self.append(item)


s22 = MyClass2()
s22.push(1)
s22.push(2)
s22.push(3)

print(f'length is {len(s22)} after push 3 items')

print(s22.pop())
print(s22.pop())
print(s22.pop())

print(f'length is {len(s22)} after pop 3 items')


print(f'verson of MyStack is {MyStack.version()}')