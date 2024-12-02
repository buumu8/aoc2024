def checkOrder(numbers):
    isDescend = True
    if numbers[0] == numbers[1]:
        return False
    if 0 < numbers[1] - numbers[0] <= 3:
        isDescend = False
    elif 0 < numbers[0] - numbers[1] <= 3:
        isDescend = True
    else:
        return False
    for x, y in zip(numbers[1:], numbers[2:]):
        if isDescend and (x - y <= 0 or x - y > 3):
            return False
        elif not isDescend and (y - x <= 0 or y - x > 3):
            isSecure = False
            return False
    return True


def part1(filename):
    with open(filename, "r") as f:
        res = 0
        for line in f:
            numbers = line.strip().split()
            numbers = [int(item) for item in numbers]
            isSecure = checkOrder(numbers)
            if isSecure:
                print(numbers)
                res += 1
        return res


def part2(filename):
    with open(filename, "r") as f:
        res = 0
        for line in f:
            numbers = line.strip().split()
            numbers = [int(item) for item in numbers]
            isSecure = checkOrder(numbers)
            if isSecure:
                print(numbers)
                res += 1
            else:
                for num in numbers:
                    dampened = numbers.copy()
                    dampened.remove(num)
                    isSecure = checkOrder(dampened)
                    if isSecure:
                        print(dampened)
                        res += 1
                        break

        return res


# print(part1("input"))
print(part2("input"))
