

def count_paths(n, memo):
    if n == 1:
        if not memo[0]:
            memo[0] = 1
        return memo[0]
    elif n == 2:
        if not memo[1]:
            memo[1] = 2
        return memo[1]
    elif n == 3:
        if not memo[2]:
            memo[2] = 4
        return memo[2]
    else:
        if not memo[n-1]:
            memo[n-1] = count_paths(n-1, memo) + count_paths(n-2, memo) + count_paths(n-3, memo)
        return memo[n-1]


if __name__ == '__main__':
    steps = 7
    print(count_paths(steps, [None]*steps))
