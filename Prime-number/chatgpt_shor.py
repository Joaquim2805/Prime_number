import numpy as np
import random

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    """Calculate the modular inverse of a modulo m."""
    g = gcd(a, m)
    if g != 1:
        raise Exception("The modular inverse does not exist")
    else:
        return pow(a, m-2, m)

def pow_mod(a, k, n):
    """Calculate a^k (mod n) using binary exponentiation."""
    result = 1
    while k > 0:
        if k & 1:
            result = (result * a) % n
        a = (a * a) % n
        k >>= 1
    return result

def order_mod(a, n):
    """Calculate the order of a modulo n."""
    t = 1
    r = 1
    while t <= n:
        r = (r * a) % n
        if r == 1:
            return t
        t += 1
    return None

def period_finding(a, n):
    """Calculate the period of a^x (mod n) using the order_mod function."""
    if gcd(a, n) != 1:
        raise Exception("The gcd of a and n must be 1")
    else:
        return order_mod(a, n)

def shor(n):
    """Factorize a number n into its prime factors."""
    if n % 2 == 0:
        return 2, n // 2
    a = random.randint(2, n-2)
    r = period_finding(a, n)
    if r % 2 == 0:
        x = pow_mod(a, r // 2, n)
        if x != 1 and x != n-1:
            p = gcd(x-1, n)
            if p > 1 and p < n:
                return p, n // p
    return None, None

def factorize(n):
    """Factorize a number n into its prime factors using the shor algorithm."""
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    p, q = shor(n)
    if p is None:
        return [n]
    else:
        return factorize(p) + factorize(q)
    


factorize(15)