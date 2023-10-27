# написать list comprehension генерации доски для шахмат. в качестве значения 0 - черный, 1 - белый.

chess_board = [0 if (i + j) % 2 else 1 for j in range(8) for i in range(8)]
print(chess_board)
