import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("inventory.json")


def load_inventory():
    if not DATA_FILE.exists():
        return {}
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            print("Предупреждение: файл данных имеет неверный формат. Начат пустой учёт.")
            return {}
        cleaned = {}
        for name, quantity in data.items():
            if isinstance(name, str) and isinstance(quantity, int) and quantity >= 0:
                cleaned[name] = quantity
        return cleaned
    except (json.JSONDecodeError, OSError):
        print("Предупреждение: не удалось прочитать файл. Начат пустой учёт.")
        return {}


def save_inventory(inventory):
    DATA_FILE.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def read_positive_quantity():
    try:
        quantity = int(input("Количество: "))
        if quantity <= 0:
            print("Количество должно быть положительным.")
            return None
        return quantity
    except ValueError:
        print("Введите целое число.")
        return None


def main():
    inventory = load_inventory()
    while True:
        command = input("\nКоманда (add/sell/list/exit): ").strip().lower()

        if command == "add":
            name = input("Название товара: ").strip()
            quantity = read_positive_quantity()
            if not name or quantity is None:
                print("Товар не добавлен: проверьте название и количество.")
                continue
            inventory[name] = inventory.get(name, 0) + quantity
            save_inventory(inventory)
            print("Товар добавлен.")

        elif command == "sell":
            name = input("Название товара: ").strip()
            quantity = read_positive_quantity()
            if quantity is None:
                continue
            if name not in inventory:
                print("Такого товара нет.")
                continue
            if quantity > inventory[name]:
                print(f"Недостаточно товара. На складе: {inventory[name]}.")
                continue
            inventory[name] -= quantity
            save_inventory(inventory)
            print("Продажа выполнена.")

        elif command == "list":
            if not inventory:
                print("Склад пуст.")
            else:
                for name, quantity in inventory.items():
                    print(f"{name}: {quantity}")

        elif command == "exit":
            print("Работа завершена.")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
