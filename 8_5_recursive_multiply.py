def multiply(x, y):
    if y == 1:
        return x
    return x + multiply(x, y - 1)


if __name__ == '__main__':
    x, y = 8, 8
    print(multiply(x, y))
