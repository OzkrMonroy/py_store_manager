import flet as ft


class Table(ft.UserControl):

    def __init__(self, page: ft.Page, cols: list, rows: list, width: int):
        super().__init__()
        self.page = page
        self.cols = cols
        self.rows = rows
        self.width = width

    def build(self):
        return ft.DataTable(
            width=self.width,
            columns=[ft.DataColumn(ft.Text("Nombre")),
                     ft.DataColumn(ft.Text("Acciones"))],
            rows=self.gen_rows(),
        )

    def gen_cols(self):
        cols = []
        for col in self.cols:
            col_data = ft.DataColumn(ft.Text(col))
            cols.append(col_data)
        return cols

    def gen_rows(self):
        rows = []
        for row_quantity in range(len(self.rows)):
            cells = self.gen_cells(self.rows[row_quantity])
            row = ft.DataRow(cells=cells)
            rows.append(row)
        return []

    def gen_cells(self, row_data):
        cells = []
        for data in row_data:
            cell = ft.DataCell(ft.Text(data))
            cells.append(cell)
        return cells

    def to_edit(self, e, element_id):
        print("To edit", element_id)
