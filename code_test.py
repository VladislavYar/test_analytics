from sys import platform


<<<<<<< HEAD
print('Не очень опасные изменения!')
=======
print('Опасные изменения.')
>>>>>>> parent of 36987dd (Main.)
if platform != 'win32':
    print('Любитель линукс или яблока?')
if platform == 'win32':
    print('Лицензия или ломанная? ПРИЗНАВАЙСЯ!')
