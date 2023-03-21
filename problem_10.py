from typing import List


def sieve_of_erastothenes(n: int) -> List:
    """Returns a list of all the prime numbers below n using the sieve of erastosthenes algorithm"""
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def prime_summation(n):
    """Returns the sum of all the primes below n"""
    return sum(sieve_of_erastothenes(n))


if __name__ == "__main__":
    # print(sieve_of_erastothenes(1000000))
    print(prime_summation(2000000))
