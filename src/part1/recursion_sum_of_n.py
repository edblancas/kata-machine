# recursive impl is also called top-bottom
def sum_of_n_rec_log(n):
    if n == 0:
        return 0
    v = sum_of_n_rec_log(n - 1) + n
    return v


def sum_of_n_rec(n):
    if n == 0:
        return 0
    return sum_of_n_rec(n - 1) + n


def sum_of_n_tail_rec(n, acc):
    if n == 1:
        return acc
    return sum_of_n_tail_rec(n - 1, acc + n)


def sum_of_n_iter(n, acc):
    acc = 0
    while True:
        if n == 0:
            return acc
        acc += n
        n -= 1


# bottom-up aka tabulation
def sum_of_n_tab(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp[n]
