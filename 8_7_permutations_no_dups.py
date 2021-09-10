def get_permutations(s):
    if len(s) == 1:
        return [s]
    perms = get_permutations(s[:-1])
    new_perms = []
    for perm in perms:
        for i in range(len(perm)+1):
            new_perms.append(perm[:i] + s[-1] + perm[i:])
    return new_perms


if __name__ == '__main__':
    s = "abcdef"
    perms = get_permutations(s)
    print(len(perms))
    print(perms)
