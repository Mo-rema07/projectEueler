from problem_3 import get_factors


def smallest_multiple(n: int) -> int:
    """Return the smallest positive number that is evenly divisible by all the numbers from 1 to n"""
    if n == 1 or n == 2:
        return n
    else:
        prev_multiple = smallest_multiple(n - 1)
        return int(prev_multiple * n / highest_common_factor(prev_multiple, n))


def highest_common_factor(a: int, b: int) -> int:
    """Returns the highest common factor of two numbers"""
    a_factors = set(get_factors(a))
    b_factors = set(get_factors(b))
    common_factors = a_factors.intersection(b_factors)
    return max(common_factors)


if __name__ == "__main__":
    # print(smallest_multiple(10))
    print(smallest_multiple(20))
