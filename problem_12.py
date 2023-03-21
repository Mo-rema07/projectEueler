def get_nth_triangular_number(n: int) -> int:
    """Returns the nth triangular number"""
    return int(n * (n + 1) / 2)


def get_number_of_divisors(n: int) -> int:
    """Returns the number of divisors of n"""
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 2
    return divisors


def get_first_triangular_number_with_n_divisors(n: int) -> int:
    """Returns the first triangular number with n divisors"""
    i = 1
    while True:
        triangular_number = get_nth_triangular_number(i)
        if get_number_of_divisors(triangular_number) > n:
            return triangular_number
        i += 1


if __name__ == "__main__":
    print(get_first_triangular_number_with_n_divisors(500))
