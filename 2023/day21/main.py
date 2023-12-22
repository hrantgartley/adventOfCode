from collections import deque
from typing import Set, Tuple


def part1():
    grid = open('input').read().splitlines()

    starting_row, starting_col = next((r, c) for r,
                                      row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S')
    final: Set[Tuple[int, int]] = set()
    seen: Set[Tuple[int, int]] = {(starting_row, starting_col)}
    final_queue: deque[Tuple[int, int, int]] = deque(
        [(starting_row, starting_col, 64)])

    while final_queue:
        row, column, start = final_queue.popleft()

        if start % 2 == 0:
            final.add((row, column))
        if start == 0:
            continue

        for new_row, new_col in [(row + 1, column), (row-1, column), (row, column+1), (row, column-1)]:
            if new_row < 0 or new_row >= len(grid) or \
                    new_col < 0 or new_col >= len(grid[0]) \
                    or grid[new_row][new_col] == "#" \
                    or (new_row, new_col) in seen:
                continue
            seen.add((new_row, new_col))
            final_queue.append((new_row, new_col, start - 1))
    print(len(final))
    # Your code here


def part2():

    grid = open('input').read().splitlines()

    sr, sc = next((r, c) for r, row in enumerate(grid)
                  for c, ch in enumerate(row) if ch == "S")

    assert len(grid) == len(grid[0])

    size = len(grid)
    STEPS = 26501365

    assert sr == sc == size // 2
    assert STEPS % size == size // 2

    def fill(sr, sc, ss):
        ans = set()
        seen = {(sr, sc)}
        q = deque([(sr, sc, ss)])

        while q:
            row, col, start = q.popleft()

            if start % 2 == 0:
                ans.add((row, col))
            if start == 0:
                continue

            for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if new_row < 0 or new_row >= len(grid) or \
                    new_col < 0 or new_col >= len(grid[0]) \
                    or grid[new_row][new_col] == "#" or (new_row, new_col) in seen:
                    continue
                seen.add((new_row, new_col))
                q.append((new_row, new_col, start - 1))

        return len(ans)

    grid_width = STEPS // size - 1

    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = fill(sr, sc, size * 2 + 1)
    even_points = fill(sr, sc, size * 2)

    corner_t = fill(size - 1, sc, size - 1)
    corner_r = fill(sr, 0, size - 1)
    corner_b = fill(0, sc, size - 1)
    corner_l = fill(sr, size - 1, size - 1)

    small_tr = fill(size - 1, 0, size // 2 - 1)
    small_tl = fill(size - 1, size - 1, size // 2 - 1)
    small_br = fill(0, 0, size // 2 - 1)
    small_bl = fill(0, size - 1, size // 2 - 1)

    large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
    large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
    large_br = fill(0, 0, size * 3 // 2 - 1)
    large_bl = fill(0, size - 1, size * 3 // 2 - 1)

    print(
        odd * odd_points +
        even * even_points + corner_t + corner_r + corner_b + corner_l +
        (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
        grid_width * (large_tr + large_tl + large_br + large_bl)
    )


if __name__ == "__main__":
    part1()
    part2()
