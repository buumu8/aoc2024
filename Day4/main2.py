with open("input", "r") as f:
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
                    print(i, j)
                    if (
                        (diagram[i - 1][j - 1] == "M" and diagram[i + 1][j + 1] == "S")
                        or (
                            diagram[i - 1][j - 1] == "S"
                            and diagram[i + 1][j + 1] == "M"
                        )
                    ) and (
                        (diagram[i - 1][j + 1] == "M" and diagram[i + 1][j - 1] == "S")
                        or (
                            diagram[i - 1][j + 1] == "S"
                            and diagram[i + 1][j - 1] == "M"
                        )
                    ):
                        sum += 1

    print(sum)
