import os
import time
directory = os.getcwd()
print(directory)

print(os.path.join('C', 'Users', 'cdkna', 'PycharmProjects', 'Ruslan1', '.venv', 'module_7_5.py'))

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.getcwd()
    filetime = os.path.getmtime('module_7_5.py')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize('module_7_5.py')
    parent_dir = os.path.dirname('/Ruslan1/.venv/module_7')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f''f'Родительская директория: {parent_dir}')