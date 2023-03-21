from problem_3 import is_prime


def get_nth_prime(n: int) -> int:
    """Returns the nth prime number"""
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes[-1]


if __name__ == "__main__":
    print(get_nth_prime(6))
    print(get_nth_prime(10001))