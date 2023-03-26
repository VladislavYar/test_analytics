from sys import platform


print('Опасные изменения. ОЧЕНЬ ОПАСНЫЕ!')
if platform != 'win32':
    print('Любитель линукс или яблока?')
