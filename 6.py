square_of_sum = sum(range(1,101))**2
sum_of_squares = sum([x**2 for x in range(1,101)])

print("%d - %d = %d" % (square_of_sum, sum_of_squares, square_of_sum-sum_of_squares))