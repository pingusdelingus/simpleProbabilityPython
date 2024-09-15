
from factorial import factorial as f

def permutation(n, r):
    if n < r:
        return 0
    else:
        return f(n) / (f(n - r))

