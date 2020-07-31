def sudoku_displayer(n):
    """
    Write a Python code to print out the given sudoku puzzle matrix in the following format.
    """
    count_outer = 0
    count_inner = 0
    for i in sudoku:
        if count_outer % 3 == 0:
            print("- - - - - - - - - - - - - - - ")
        count_outer += 1
        for j in i:
            print(j, end="  ")
            count_inner += 1
            if count_inner % 3 == 0 and count_inner % 9 != 0:
                print("|", end=" ")

        print()
    print("- - - - - - - - - - - - - - - ")

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

sudoku_displayer(sudoku)
