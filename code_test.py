from sys import platform


print('Не очень опасные изменения!')
print('Опасные изменения.')
if platform != 'win32':
    print('Любитель линукс или яблока?')
