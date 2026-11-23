class Table:
    def __init__(self, headers=None, rows=None, col_types=None):
        self.headers = list(headers) if headers is not None else []
        self.rows = list(rows) if rows is not None else []

        col_count = (len(self.headers) if self.headers else (len(self.rows[0])) if self.rows else 0)

        if col_types is not None:
            self.col_types = dict(col_types)
        else:
            self.col_types = {i: str for i in range(col_count)}