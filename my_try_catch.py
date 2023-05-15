
filename = '没这个文件.txt'

try:
    with open(filename, 'r') as f:
        print(f.readline())
except FileNotFoundError:
    print(f'文件虽然没找到，但是程序也没崩。')



# try:
#     f = open(file=filename)
#     print(f.readline())
# except FileNotFoundError as err:
#     print(f'文件虽然没找到，但是程序也没崩。')
# finally:
#     if f:
#         f.close()
#     print('不管执行是不是成功，文件到最后都得关掉。')

