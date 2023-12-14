grid = tuple(open('input').read().splitlines())


def cycle():
    global grid
    # transforms the grid 90 degrees clockwise each iteration
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)


seen = {grid}
array = [grid]

iter = 0

while True:
    iter += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)

grid = array[(1000000000 - first) % (iter - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
