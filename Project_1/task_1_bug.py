def main():
    direction = input("Направление (C = Цельсий в Фаренгейт, F = Фаренгейт в Цельсий): ").strip().upper()
    try:
        temperature = float(input("Введите температуру: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return

    if direction == "C":
        result = temperature * 9 / 5  # ДЕФЕКТ: пропущено +32
        print(f"Результат: {result:.2f} °F")
    elif direction == "F":
        result = (temperature - 32) * 5 / 9
        print(f"Результат: {result:.2f} °C")
    else:
        print("Ошибка: выберите C или F.")


if __name__ == "__main__":
    main()
