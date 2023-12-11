with open("input") as file:
    input = file.read().splitlines()

    columns = {}
    rows = {}
    # expand vertically
    for row in range(len(input)):
        if input[row].count('#') == 0:
            # 0 above means expand
            rows[row] = True
        else:
            rows[row] = False

            # input.insert(row,'.'*len(input[row]))
    # expand horizontally
    for col in range(len(input[0])):
        expand = True
        for row in range(len(input)):
            if input[row][col] == "#":
                expand = False
        if expand:
            columns[col] = True
        else:
            columns[col] = False

    answer = 0
    answer2 = 0
    part2_expansion = 1000000
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == "#":
                for yb in range(len(input)):
                    for xb in range(len(input[0])):
                        if input[yb][xb] == "#":
                            if yb > y:
                                for row in range(y, yb):
                                    if rows[row]:
                                        answer += 2
                                        answer2 += part2_expansion
                                    else:
                                        answer += 1
                                        answer2 += 1
                            if yb < y:
                                for row in range(yb, y):
                                    if rows[row]:
                                        answer += 2
                                        answer2 += part2_expansion
                                    else:
                                        answer += 1
                                        answer2 += 1
                            if xb > x:
                                for col in range(x, xb):
                                    if columns[col]:
                                        answer += 2
                                        answer2 += part2_expansion
                                    else:
                                        answer += 1
                                        answer2 += 1
                            if xb < x:
                                for col in range(xb, x):
                                    if columns[col]:
                                        answer += 2
                                        answer2 += part2_expansion
                                    else:
                                        answer += 1
                                        answer2 += 1

    print(answer//2)
    print(answer2//2)
