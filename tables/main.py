import csv_module, pickle_module, txt_module


my_table = {
    'headers': ['ID', 'Имя', 'Возраст'],
    'rows': [
        ['1', 'Алексей', '25'],
        ['2', 'Мария', '30'],
        ['3', 'Иван', '22'],
    ],
}


csv_module.save_table(my_table, 'data.csv')
pickle_module.save_table(my_table, 'data.pkl')
txt_module.save_table(my_table, 'data.txt')

loaded_table = csv_module.load_table('data.csv')
txt_module.print_table(loaded_table)
