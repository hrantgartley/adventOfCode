import sympy
from day24_class import Hailstone


def part1():
    hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in open('input')]

    total = 0

    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            a1, b1, c1 = hs1.a, hs1.b, hs1.c
            a2, b2, c2 = hs2.a, hs2.b, hs2.c
            if a1 * b2 == b1 * a2:
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                    total += 1

    print(total)


def part2():
    answer = None
    hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open('input')]

    final_x, final_y, final_z, final_vx, final_vy, final_vz = sympy.symbols("final_x final_y final_z final_vx final_vy final_vz")

    position_equations = []
    final_positions = []

    for index, (stone_x, stone_y, stone_z, stone_vx, stone_vy, stone_vz) in enumerate(hailstones):
        position_equations.append((final_x - stone_x) * (stone_vy - final_vy) - (final_y - stone_y) * (stone_vx - final_vx))
        position_equations.append((final_y - stone_y) * (stone_vz - final_vz) - (final_z - stone_z) * (stone_vy - final_vy))

        if index < 2:
            continue

        solutions = sympy.solve(position_equations)
        integer_solutions = [sol for sol in solutions if all(val % 1 == 0 for val in sol.values())] if solutions else []

        if len(integer_solutions) == 1:
            final_positions = integer_solutions
            break

    if final_positions:
        answer = final_positions[0]
        result = answer.get(final_x, 0) + answer.get(final_y, 0) + answer.get(final_z, 0)
        print(result)


if __name__ == "__main__":
    part1()
    part2()
