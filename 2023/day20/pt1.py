from collections import deque
from day20_class import Module


def main():
    modules = {}
    broadcast_targets = []

    for line in open('input'):
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    lo = hi = 0

    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                lo += 1
            else:
                hi += 1

            if target not in modules:
                continue

            module = modules[target]

            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    if module.memory == "on":
                        outgoing = "hi"
                    else:
                        outgoing = "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(
                    x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

        print(lo * hi)
        # Your code here


if __name__ == "__main__":
    main()
