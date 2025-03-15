import os
from datetime import datetime


def write_file_info_to_text(output_file):
    files = os.listdir()

    with open(output_file, 'w') as f:
        for file in files:
            if os.path.isfile(file):
                size = os.path.getsize(file)

                modification_time = os.path.getmtime(file)
                modification_time_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

                f.write(f"Файл: {file}\n")
                f.write(f"Размер: {size} байт\n")
                f.write(f"Последнее изменение: {modification_time_str}\n")
                f.write("\n")

    print(f"Информация о файлах записана в '{output_file}'.")

output_file = 'inf.txt'

if __name__ == '__main__':
    write_file_info_to_text(output_file)
