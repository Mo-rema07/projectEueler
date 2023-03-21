from typing import List


def get_prime_factors(n: int) -> List:
    """Returns all the prime factors of a positive integer"""
    p_factors = []
    f = get_factors(n)
    for i in f:
        if is_prime(i):
            p_factors.append(i)
    return p_factors


def get_factors(n: int) -> List:
    """Returns all the factors of a positive integer"""
    f = []
    n = int(n)
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f


def is_prime(n: int) -> bool:
    """Returns True if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(max(get_prime_factors(600851475143)))
