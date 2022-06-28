def gcd(a: int, b: int) -> int:
    """O(log min(a,b))"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """O(log min(a,b))"""
    return a // gcd(a, b) * b
