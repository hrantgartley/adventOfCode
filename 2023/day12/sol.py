def part1():
    def count(cfg, nums):
        if cfg == "":
            return 1 if nums == () else 0

        if nums == ():
            return 0 if "#" in cfg else 1

        result = 0

        if cfg[0] in ".?":
            result += count(cfg[1:], nums)

        if cfg[0] in "#?":
            if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                result += count(cfg[nums[0] + 1:], nums[1:])

        return result

    total = 0

    for line in open("input"):
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        total += count(cfg, nums)

    print(total)


def part2():
    cache = {}

    def count(cfg, nums):
        if cfg == "":
            return 1 if nums == () else 0

        if nums == ():
            return 0 if "#" in cfg else 1

        key = (cfg, nums)

        if key in cache:
            return cache[key]

        result = 0

        if cfg[0] in ".?":
            result += count(cfg[1:], nums)

        if cfg[0] in "#?":
            if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                result += count(cfg[nums[0] + 1:], nums[1:])

        cache[key] = result
        return result

    total = 0

    for line in open("input"):
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        cfg = "?".join([cfg] * 5)
        nums *= 5

        total += count(cfg, nums)

    print(total)


if __name__ == "__main__":
    part1()
    part2()
