def hash_function(s):
    value = 0
    for character in s:
        value += ord(character)
        value *= 17
        value %= 256
    return value


def part1():
    print(sum(map(hash_function, input().split(','))))
    # with open(sys.argv[1]) as f:
    #     print(sum(map(hash, f.read().split(','))))
    # print(sum(map(hash, open(sys.argv[1]).read().split(','))))


def part2():
    print("This is main.py for 2023 Day 15")
    print(hash_function("Hello World!"))


if __name__ == "__main__":
    part1()
    part2()
