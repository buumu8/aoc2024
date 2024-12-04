with open("test", "r") as f:
    text = []
    for line in f:
        text.append(line.strip())
    sum = 0
    if len(text) > 0:
        nrow = len(text)
        ncol = len(text[0])
        for i in range(nrow):
            for j in range(ncol):
                print(text[i][j])
