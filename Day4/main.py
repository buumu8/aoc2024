def part1(filename):
    with open(filename, "r") as f:
        diagram = []
        for line in f:
            diagram.append(line.strip())
        sum = 0
        if len(diagram) > 0:
            nrow = len(diagram)
            ncol = len(diagram[0])
            for i in range(nrow):
                for j in range(ncol):
                    if diagram[i][j] == "X":
                        nexts = ["M", "A", "S"]
                        directions = [
                            (0, 1),
                            (1, 1),
                            (1, 0),
                            (1, -1),
                            (0, -1),
                            (-1, -1),
                            (-1, 0),
                            (-1, 1),
                        ]
                        for x, y in directions:
                            temp = "X"
                            if 0 <= i + x < nrow and 0 <= j + y < ncol:
                                multiplyer = 1
                                for letter in nexts:
                                    if (
                                        0 <= i + x * multiplyer < nrow
                                        and 0 <= j + y * multiplyer < ncol
                                    ):
                                        if (
                                            diagram[i + x * multiplyer][
                                                j + y * multiplyer
                                            ]
                                            != letter
                                        ):
                                            break
                                        temp += letter
                                    multiplyer += 1
                            else:
                                continue
                            if temp == "XMAS":
                                sum += 1
        return sum


def part2(filename):
    with open(filename, "r") as f:
        diagram = []
        for line in f:
            diagram.append(line.strip())
        sum = 0
        if len(diagram) > 0:
            nrow = len(diagram)
            ncol = len(diagram[0])
            for i in range(1, nrow - 1):
                for j in range(1, ncol - 1):
                    if diagram[i][j] == "A":
                        if (
                            (
                                diagram[i - 1][j - 1] == "M"
                                and diagram[i + 1][j + 1] == "S"
                            )
                            or (
                                diagram[i - 1][j - 1] == "S"
                                and diagram[i + 1][j + 1] == "M"
                            )
                        ) and (
                            (
                                diagram[i - 1][j + 1] == "M"
                                and diagram[i + 1][j - 1] == "S"
                            )
                            or (
                                diagram[i - 1][j + 1] == "S"
                                and diagram[i + 1][j - 1] == "M"
                            )
                        ):
                            sum += 1
        return sum


# print(part1("input"))
print(part2("input"))
