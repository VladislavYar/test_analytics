from sys import platform


print('Опасные изменения.')
if platform != 'win32':
    print('Любитель линукс или яблока?')
if platform == 'win32':
    print('Лицензия или ломанная? ПРИЗНАВАЙСЯ!')
