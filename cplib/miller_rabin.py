# Originated from https://zenn.dev/mizar/articles/791698ea860581
# Verify https://algo-method.com/tasks/513


def is_prime(n: int):
    """Miller-Rabin: ≒ O(1)"""
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    n1 = n - 1
    d, s = n1, 0
    while (d & 1) == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        t = pow(a, d, n)
        if t == 1 or t == n1:
            continue
        for _ in range(s - 1):
            t = pow(t, 2, n)
            if t == n1:
                break
        else:
            return False
    return True
