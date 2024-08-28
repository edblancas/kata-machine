# to understand well recursion we need:
# 1. return address: where the current call returns to and hand out the value
# 2. return value: we have to return a vaulue and what most matter, make space for it
# 3. arguments: pass things into the fn, so we put that memory into our system

# the recursion call has: 
# 1. pre: for doing things before the recursion, in this example is only `n +`
# 2. recurse: actually does the calling of the fn
# 3. post: like doing log; in the sum_of_n_rec we don't do anything, 
#       in the sum_of_n_rec_log we log

def sum_of_n_rec_log(n):
    if n == 0:
        return 1
    out = n + sum_of_n_rec_log(n - 1)
    print(n)
    return out

# this is not tail recursive, and uses the stack frame to save the args, so
# it adds up to the space complexity
def sum_of_n_rec(n):
    if n == 0:
        return 1  # cuz the base case o sum(1) is 1
    return n + sum_of_n_rec(n - 1)

# this is tail recursive, but python3 doesn't has tail rec optimization, so is
# the same space complexity as the above, you must manually convert this to
# an iterative way
def sum_of_n_tail_rec(n, acc):
    if n == 0:
        return acc
    return sum_of_n_tail_rec(n - 1, acc + n)

# form the tail rec, is easy to make it iterative, it is just a goto
# there is no goto in python3, but the code below is the same
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
