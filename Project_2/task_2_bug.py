PASSING_SCORE = 4.5


def main():
    raw = input("Введите оценки от 1 до 5 через пробел: ").strip()
    parts = raw.split()
    if not parts:
        print("Ошибка: список оценок пуст.")
        return

    try:
        grades = [int(part) for part in parts]
    except ValueError:
        print("Ошибка: все оценки должны быть целыми числами.")
        return

    if any(grade < 1 or grade > 5 for grade in grades):
        print("Ошибка: оценки должны быть от 1 до 5.")
        return

    average = sum(grades) // len(grades)  # ДЕФЕКТ: целочисленное деление
    status = "Зачёт" if average >= PASSING_SCORE else "Незачёт"
    print(f"Средний балл: {average:.2f}")
    print(status)


if __name__ == "__main__":
    main()
