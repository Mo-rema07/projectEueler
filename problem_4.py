def largest_palindrome_product(n: int) -> int:
    """Returns the largest palindrome made from the product of two n-digit numbers"""
    largest = 0
    for i in range(10 ** (n - 1), 10 ** n):
        for j in range(10 ** (n - 1), 10 ** n):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest:
                largest = product
    return largest


if __name__ == "__main__":
    print(largest_palindrome_product(2))
    print(largest_palindrome_product(3))
    print(largest_palindrome_product(4))