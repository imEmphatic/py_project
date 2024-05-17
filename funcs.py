def summ_numbers():
    print("Давайте сложим два числа\n")
    user_first_number = int(input("Введите первое число: "))
    user_second_number = int(input("Введите второе число: "))

    print(f"\nРезультат: {user_first_number + user_second_number}\n")


if __name__ == "__main__":
    summ_numbers()


def subtraction_numbers():
    print("Давайте найдём разницу двух чисел\n")
    user_first_number = int(input("Введите первое число: "))
    user_second_number = int(input("Введите второе число: "))

    print(f"\nРезультат: {user_first_number - user_second_number}\n")


if __name__ == "__main__":
    subtraction_numbers()
