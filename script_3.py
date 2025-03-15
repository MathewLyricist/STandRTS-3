def find_min_max(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit() or (line.strip()[1:].isdigit() and line.strip()[0] in ['-', '+'])]

        if not numbers:
            raise ValueError("Файл не содержит целых чисел.")

        min_number = min(numbers)
        max_number = max(numbers)

        with open(output_file, 'w') as f_out:
            f_out.write(f"Минимальное число: {min_number}\n")
            f_out.write(f"Максимальное число: {max_number}\n")

        print(f"Минимальное и максимальное числа записаны в {output_file}.")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

input_file = 'z3.1-1.txt'
output_file = 'srez.txt'

if __name__ == '__main__':
    find_min_max(input_file, output_file)
