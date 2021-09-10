def move_disks(n, origin, buffer, destination):
    # base case
    if n <= 0:
        return
    # recursive case
    # move first n-1 disks to tower 2
    move_disks(n - 1, origin, destination, buffer)
    # move nth disk to tower 3
    x = origin.pop()
    destination.append(x)
    # move n-1 disks to tower 3
    move_disks(n - 1, buffer, origin, destination)


if __name__ == '__main__':
    n = 5
    tower_1 = list(range(n, 0, -1))
    tower_2 = []
    tower_3 = []
    move_disks(n, tower_1, tower_2, tower_3)
    print(tower_1)
    print(tower_2)
    print(tower_3)
