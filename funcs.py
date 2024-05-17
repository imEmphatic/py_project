def summ():
    print("Давайте сложим два числа\n")
    user_first_number = int(input("Введите первое число: "))
    user_second_number = int(input("Введите второе число: "))

    print(f"\nРезультат: {user_first_number + user_second_number}")


if __name__ == "__main__":
    summ()