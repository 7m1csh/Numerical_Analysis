# Algorithm 6-7 連分数展開に対応する有理式の計算
"""
Input: a1, a2, ..., an, b0, b1, ..., bn
Output: P, Q
P(-1) <- 1, P(0) <- b(0)
Q(-1) <- 0, Q(0) <- 1
for k=0 to n-1
    P(k+1) <-  b(k+1)*P(k) + a(k+1)*P(k-1)
    Q(k+1) <-  b(k+1)*Q(k) + a(k+1)*Q(k-1)
end for
"""
def continued_fraction_to_rational(a, b):
    n = len(a) - 1  # a[0] is b0, a[1:] are a1, a2, ..., an
    P = [0] * (n + 2)  # P will hold P(-1), P(0), ..., P(n)
    Q = [0] * (n + 2)  # Q will hold Q(-1), Q(0), ..., Q(n)

    # Initial conditions
    P[0] = 1
    P[1] = b[0]
    Q[0] = 0
    Q[1] = 1

    for k in range(n):
        P[k + 2] = b[k + 1] * P[k + 1] + a[k + 1] * P[k]
        Q[k + 2] = b[k + 1] * Q[k + 1] + a[k + 1] * Q[k]

    return P, Q

# Example usage
if __name__ == "__main__":
    a = [1, 1, 1, 1, 1]
    b = [1, 1, 1, 1, 1]
    P, Q = continued_fraction_to_rational(a, b)
    print(f"P(-1), P(0), P(1), ... P(n): {P}, Q(-1), Q(0), Q(1), ...Q(n): {Q}")

