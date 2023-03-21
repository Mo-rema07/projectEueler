def even_fibonacci_sum(n):
    """Return the sum of all even Fibonacci numbers less than n."""
    a, b = 0, 1
    even_list = []
    while b < n:
        if b % 2 == 0:
            even_list.append(b)
        a, b = b, a + b
    return sum(even_list)


if __name__ == "__main__":
    print(even_fibonacci_sum(4000000))
