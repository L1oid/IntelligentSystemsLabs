def print_operation_table(operation, num_rows = 9, num_columns = 9):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end="\t")
        print()

print_operation_table(lambda x, y: x * y)
