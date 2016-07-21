from db import *
from os import remove
remove('my.db')
f.open('my.db')
f.close()
user.create_table()
print('таблички созданы')
