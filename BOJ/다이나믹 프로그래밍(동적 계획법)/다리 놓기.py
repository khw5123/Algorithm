import math

def nCr(n, r):
    f = math.factorial
    return f(n) // (f(r)*f(n-r))

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(nCr(m, n))