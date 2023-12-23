def part1():
    grid = open('input').read().splitlines()

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for new_row, new_col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    graph = {pt: {} for pt in points}

    dirs = {
        "^": [(-1, 0)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    for sr, sc in points:
        stack = [(0, sr, sc)]
        stack: list[tuple[int, int, int]]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in dirs[grid[r][c]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    print(dfs(start))    # Your code here


def part2():
    grid = open('input').read().splitlines()

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        stack: list[tuple[int, int, int]]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    print(dfs(start))


if __name__ == "__main__":
    part1()
    part2()
