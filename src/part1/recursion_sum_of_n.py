# this is not tail recursive, and uses the stack frame to save the args, so
# it adds up to the space complexity
def sum_of_n_rec(n):
    if n == 0:
        return n
    return sum_of_n_rec(n - 1) + n

# this is tail recursive, but python3 doesn't has tail rec optimization, so is
# the same space complexity as the above, you must manually convert this to
# an iterative way
def sum_of_n_tail_rec(n, acc):
    if n == 0:
        return acc
    return sum_of_n_tail_rec(n - 1, acc + n)

# form the tail rec, is easy to make it iterative, it is just a goto
# C code, you can see the translation very clearly without the decrement and +=
# operator
# int sum_iter(int n, int acc) {
#     top:
#         if (n == 0) return acc;
#         acc = acc + n;  // acc += n;
#         n = n - 1  // n--;
#         goto top;
# }
def sum_of_n_iter(n, acc):
    while True:
        if n == 0:
            return acc
        acc = acc + n
        n = n - 1
