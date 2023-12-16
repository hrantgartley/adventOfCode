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
    boxes = [[] for _ in range(256)]
    focal_lengths = {}

    for instruction in input().split(","):
        if "-" in instruction:
            label = instruction[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = instruction.split("=")
            length = int(length)
            
            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)
                
            focal_lengths[label] = length

    total = 0

    for box_number, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            total += box_number * lens_slot * focal_lengths[label]

    print(total)



if __name__ == "__main__":
    # part1()
    part2()
