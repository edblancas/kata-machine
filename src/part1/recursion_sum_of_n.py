# recursive impl is also called top-bottom

# add a log before returning
def sum_of_n_rec_log(n):
    if n == 0:
        return 0
    out = n + sum_of_n_rec_log(n - 1)
    print(out)
    return out


def sum_of_n_rec(n):
    if n == 1:
        return 1
    return n + sum_of_n_rec(n - 1)


def sum_of_n_tail_rec(n, acc):
    if n == 0:
        return acc
    return sum_of_n_tail_rec(n - 1, acc + n)


def sum_of_n_iter(n, acc):
    while True:
        if n == 0:
            return acc
        acc = acc + n
        n = n - 1


# bottom-up aka tabulation aka dynamic programming
# This approach builds a table (dp) where dp[i] stores the sum of numbers from 1 to i. It iteratively fills the table using the recurrence relation: dp[i]=dp[i−1]+i
def sum_of_n_tab(n):
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        table[i] = table[i - 1] + i
    return table[n]
