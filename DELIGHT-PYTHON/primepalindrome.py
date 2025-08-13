def is_palindromic_prime(n):
    if n < 2:
        return False
    if str(n) != str(n)[::-1]:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True