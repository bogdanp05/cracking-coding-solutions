def get_power_set(xs):
    # base case
    if len(xs) == 1:
        return [[], [xs[0]]]
    # recursive case
    power_set = get_power_set(xs[:-1])
    for s in power_set.copy():
        power_set.append(s + [xs[-1]])
    return power_set


if __name__ == '__main__':
    elems = [1, 2, 3, 4, 5, 6]
    power_set = get_power_set(elems)
    print(power_set)
    print(len(power_set))
