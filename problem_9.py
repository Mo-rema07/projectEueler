def get_special_pythagorean_triplet(n: int) -> int:
    """Returns the product of the Pythagorean triplet whose sum is n"""
    for a in range(1, n):
        for b in range(1, n):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 0


if __name__ == "__main__":
    print(get_special_pythagorean_triplet(1000))
