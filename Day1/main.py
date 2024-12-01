def part1():
    with open("input", "r") as file:
        list1, list2 = [], []
        for line in file:
            num1, num2 = line.strip().split()
            list1.append(int(num1))
            list2.append(int(num2))
        list1.sort()
        list2.sort()
        res = 0
        for index, value in enumerate(list1):
            res += abs(value - list2[index])
        print(f"part1: {res}")


def part2():
    with open("input", "r") as file:
        map = {}
        list1, list2 = [], []
        res = 0
        for line in file:
            num1, num2 = line.strip().split()
            map[num1] = 0
            list1.append(num1)
            list2.append(num2)
        for item in list2:
            if item in map:
                map[item] += 1
        for num in list1:
            res += int(num) * map[num]
        print(f"part2: {res}")


part1()
part2()
