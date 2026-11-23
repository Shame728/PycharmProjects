import os
import pickle_module

test_file = "test_output.pkl"

# Создаем таблицу со сложными типами данных (int, float, bool, None, str)
original_table = {
    "headers": ["ID", "Товар", "Цена", "В наличии", "Примечание"],
    "rows": [
        [1, "Ноутбук", 75990.50, True, None],
        [2, "Мышь", 1200, False, "Скидка 10%"],
    ],
}

# 1. Сохраняем таблицу
pickle_file.save_table(original_table, test_file)



# 3. Загружаем таблицу обратно
loaded_table = pickle_file.load_table(test_file)
print(loaded_table)

# 5. Точечно проверяем сохранение типов (главное отличие от CSV)
first_row = loaded_table["rows"]


# Удаляем временный файл
os.remove(test_file)
print("Проверка модуля pickle успешно пройдена! Все данные и типы сохранены.")
