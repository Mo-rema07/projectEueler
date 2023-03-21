def sum_of_first_n_squares(n: int) -> int:
    """Returns the sum of the first n squares."""
    return sum([x ** 2 for x in range(1, n + 1)])


def square_of_sum_of_first_n(n: int) -> int:
    """Returns the square of the sum of the first n numbers."""
    return sum([x for x in range(1, n + 1)]) ** 2


def difference_of_first_n_squares(n: int) -> int:
    """Returns the difference between the sum of the squares of the first n numbers and the square of the sum of the
    first n numbers."""
    return square_of_sum_of_first_n(n) - sum_of_first_n_squares(n)


if __name__ == "__main__":
    print(difference_of_first_n_squares(10))
    print(difference_of_first_n_squares(100))
