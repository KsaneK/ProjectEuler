import time

with open('data') as f:
    matrix = f.read().split("\n")
    matrix = [list(map(int, v.split(","))) for v in matrix]

memory = {}

def min_two_ways(matrix, row=0, column=0):
    if (row, column) in memory:
        return memory.get((row, column))
    if row < 79 and column < 79:
        res = matrix[row][column] + min(min_two_ways(matrix, row, column + 1), min_two_ways(matrix, row + 1, column))

    elif row < 79:
        res = matrix[row][column] + min_two_ways(matrix, row + 1, column)

    elif column < 79:
        res = matrix[row][column] + min_two_ways(matrix, row, column + 1)

    else:
        res = matrix[row][column]

    memory[(row, column)] = res
    return res


start = time.time()

result = min_two_ways(matrix)

stop = time.time()
print("Result:", result)
print("Time:", stop - start)
