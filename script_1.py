
def first_print():
    n = int(input("Введите число n (n < 10): "))

    # Проверяем, что n меньше 10
    if n >= 10:
        print("Число должно быть меньше 10!")
    else:
        # Печатаем n строк
        for i in range(n):
            # Создаем строку с символами '$'
            line = "$" + " " * (i) + "$" + " " * (n - i - 1)
            print(line)

if __name__ == '__main__':
    first_print()