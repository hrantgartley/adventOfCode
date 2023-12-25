import math
import random


def part1():
    V = set()
    E = set()

    for line in open('input'):
        v, *ws = line.replace(':', ' ').split()
        V |= {v, *ws}
        E |= {(v, w) for w in ws}

    def ss(v): return next(s for s in subsets if v in s)

    while True:
        subsets = [{v} for v in V]

        while len(subsets) > 2:
            s1, s2 = map(ss, random.choice([*E]))
            if s1 != s2:
                s1 |= s2
                subsets.remove(s2)
        if sum(ss(u) != ss(v) for u, v in E) < 4:
            break

    print(math.prod(map(len, subsets)))


def part2():
    print("Advent of Code 2023 complete... not part2 for this section")


if __name__ == "__main__":
    part1()
    part2()
