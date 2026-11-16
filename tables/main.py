import csv_file, pickle_file, txt_file
data= {
    "headers": ["ID", "Товар", "Описание"],
    "rows": [
        [1, "Ноутбук", "Мощный, легкий"],  # Запятая внутри ячейки
        [2, 'Монитор "Pro"', "27 дюймов"],  # Кавычки внутри ячейки
    ],
}
file = csv_file.load_table('files/csv_read.csv')

print(file)

csv_file.save_table(data, 'files/output.csv')