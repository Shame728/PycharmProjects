import sys


from typing import List, Any, Optional

class Tables:
    def __init__(self, headers: List[str], rows: List[List[Any]], types: Optional[List[type]] = None ):
        if not headers:
            raise ValueError('Спикок заглавий не может быть пустым')
        for i, row in enumerate(rows):
            if len(row) != len(headers):
                raise ValueError(f'Размер строки {i} {len(row)} не совпадает с количеством заголовков {len(headers)}')
        self.headers = headers
        self.rows = rows

        if types is None:
            if rows:
                self.types = [type(x) for x in rows[0]]
            else:
                self.types = [str] * len(headers)
        else:
            if len(types) != len(headers):
                raise ValueError('Количество типов не совпадает с количеством заголовков')
            self.types = types

    def check_types(self):
        for row_id, row in enumerate(self.rows):
            for col_id, item in enumerate(row):
                expected_type = self.types[col_id]
                if not isinstance(item, expected_type):
                    raise ValueError(
                        f'Ошибка типа в строке {row_id} в колонке {self.headers[col_id]}'
                        f'Ожидался {expected_type.__name__} получен {type(item).__name__}'
                    )

    def print_table(self, table: Table, file=sys.stdout):
        if not self.headers:
            return 0

        all_rows = [table.headers] + [[str(item) for item in row] for row in table.rows]
        col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(table.headers))]

        format_str = ' | '.join(f"{{:<{w}}}" for w in col_widths)
        separator = "-+-".join("-" * w for w in col_widths)

        print(format_str.format(*table.headers), file=file)
        print(separator, file=file)
        for row in table.rows:
            print(format_str.format(*[str(item) for item in row]), file=file)
