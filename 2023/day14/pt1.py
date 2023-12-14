def part1():
    grid = open('input').read().splitlines()
    grid = list(map("".join, zip(*grid)))
    grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
    grid = list(map("".join, zip(*grid)))

    print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


if __name__ == "__main__":
    part1()
