from collections import deque


def part1():
    bricks = [
        list(map(int, line.replace("~", ",").split(","))) for line in open("input")
    ]
    bricks.sort(key=lambda brick: brick[2])

    def overlaps(a, b):
        return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

    for i, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:i]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
    bricks.sort(key=lambda brick: brick[2])

    k_supp = {i: set() for i in range(len(bricks))}
    v_supp = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supp[i].add(j)
                v_supp[j].add(i)

    total = 0
    for i in range(len(bricks)):
        if all(len(v_supp[j]) >= 2 for j in k_supp[i]):
            total += 1
    print(total)


def part2():
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in open(0)]
    bricks.sort(key=lambda brick: brick[2])

    def overlaps(a, b):
        return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    bricks.sort(key=lambda brick: brick[2])

    k_supp = {i: set() for i in range(len(bricks))}
    v_sup = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supp[i].add(j)
                v_sup[j].add(i)

    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in k_supp[i] if len(v_sup[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            for k in k_supp[j] - falling:
                if v_sup[k] <= falling:
                    q.append(k)
                    falling.add(k)

        total += len(falling) - 1

    print(total)


if __name__ == "__main__":
    part1()
    part2()
