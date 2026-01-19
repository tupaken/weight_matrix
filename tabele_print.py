def table_print(table, col_width=6):
    separator = "+" + "+".join("-" * (col_width + 2) for _ in table[0]) + "+"

    print(separator)
    for i, row in enumerate(table):
        print("| " + " | ".join(f"{str(cell):^{col_width}}" for cell in row) + " |")
        print(separator)