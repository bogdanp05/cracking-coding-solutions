def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def is_palindrome_permutation(string):
    # dictionary counting # of appearances of a char in the string
    # true means odd, false means even
    d = dict()
    odds_count = 0
    for c in string:
        d[c] = not d.get(c, False)
        if not d[c]:
            odds_count -= 1
        else:
            odds_count += 1

    return odds_count <= 1


if __name__ == '__main__':
    # print(is_palindrome_permutation("tactcoab"))
    bla = "abcdef"
    print(bla[0:2])
