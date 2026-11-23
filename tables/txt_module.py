def format_table(table):
    headers = table.get('headers', [])
    rows = table.get('rows', [])

    if not headers and not rows:
        return None

    all_rows = ([headers] if headers else []) + rows
    all_count = max(len(row) for row in all_rows)

    width = [0] * all_count
    for row in all_rows:
        for i, val in enumerate(row):
            width[i] = max(width[i], len(str(val)))

    formated_lines = []
    if headers:
        header_line = ' | '.join(str(headers[i]).ljust(width[i]) for i in range(len(headers)))
        formated_lines.append(header_line)
        formated_lines.append('-' * len(header_line))

    for row in rows:
        row_line = (' | ').join(str(row[i]).ljust(width[i]) for i in range(len(row)))
        formated_lines.append(row_line)

    return '\n'.join(formated_lines)


def print_table(table):
    print(format_table(table))


def save_table(table, file):
    formated = format_table(table)
    with open(file, mode='w', encoding='utf-8') as f:
        f.write(formated + '\n')

