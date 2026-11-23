import csv

delimiter = ','
def load_table(file):
    with open(file, newline='', encoding='utf-8', mode='r') as csv_file:
        reading = csv.reader(csv_file)
        data = list(reading)

    if not data:
        return {
            'headers': [], 'rows': []
        }
    return {
        'headers':data[0], 'rows':data[1:]
    }


def save_table(table, file_path):
    with open(file_path, newline='', encoding='utf-8', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter, quoting=csv.QUOTE_ALL)
        if table.get('headers'):
            writer.writerow(table['headers'])
        writer.writerows(table.get('rows', []))
