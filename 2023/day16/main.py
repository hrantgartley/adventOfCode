def part1():
    from collections import deque
    from typing import Deque, List, Set, Tuple

    grid = open('input').read().splitlines()

# r, c, dr, dc
    a: List[Tuple[int, int, int, int]] = [(0, -1, 0, 1)]
    seen: Set[Tuple[int, int, int, int]] = set()
    q: Deque[Tuple[int, int, int, int]] = deque(a)

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

    else:
        coords = {(r, c) for (r, c, _, _) in seen}
        print("part 1", len(coords))


def part2():
    from collections import deque

    grid = open('input').read().splitlines()

    def calc(r, c, dr, dc):
        # r, c, dr, dc
        a = [(r, c, dr, dc)]
        seen = set()
        q = deque(a)

        while q:
            r, c, dr, dc = q.popleft()

            r += dr
            c += dc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            ch = grid[r][c]

            if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "/":
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "\\":
                dr, dc = dc, dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            else:
                for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                    if (r, c, dr, dc) not in seen:
                        seen.add((r, c, dr, dc))
                        q.append((r, c, dr, dc))

        coords = {(r, c) for (r, c, _, _) in seen}

        return len(coords)

    max_val = 0

    for r in range(len(grid)):
        max_val = max(max_val, calc(r, -1, 0, 1))
        max_val = max(max_val, calc(r, len(grid[0]), 0, -1))

    for c in range(len(grid)):
        max_val = max(max_val, calc(-1, c, 1, 0))
        max_val = max(max_val, calc(len(grid), c, -1, 0))

    print(f"part 2 {max_val}")


if __name__ == "__main__":
    part1()
    part2()
