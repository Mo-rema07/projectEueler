def multiples_of_3_or_5(n):
    """Return the sum of all multiples of 3 or 5 below n."""
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


if "__main__" == __name__:
    print(multiples_of_3_or_5(1000))
