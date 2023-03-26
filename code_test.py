from datetime import datetime
from sys import platform


print(datetime.now())
if platform == 'win32':
    print('Лицензия или ломанная? ПРИЗНАВАЙСЯ!')
