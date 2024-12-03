import re

# ******* PART1 ************


def find_expressions(input_text):
    pattern = r"mul\(\d+,\d+\)"
    return re.findall(pattern, input_text)


def multiply(exp):
    pattern = r"\d+"
    numbers = re.findall(pattern, exp)
    print(numbers)
    return int(numbers[0]) * int(numbers[1])


def part1(filename):
    with open(filename, "r") as f:
        text = f.read()
        expressions = find_expressions(text)
        sum = 0
        for exp in expressions:
            sum += multiply(exp)
        print(sum)


# ******* PART2 ************


def find_dont(input_text):
    return input_text.index("don't()") if "don't()" in input_text else -1


def find_do(input_text):
    return input_text.index("do()") if "do()" in input_text else -1


def part2(filename):
    with open(filename, "r") as f:
        text = f.read()
        expressions = find_expressions(text)
        start_index = 0
        sum = 0
        dont_flag = False
        while len(expressions) > 0:
            exp = expressions[0]
            exp_index = text.index(exp) + len(exp)
            dont_index = find_dont(text[start_index:exp_index])
            do_index = find_do(text[start_index:exp_index])
            if dont_index > -1:
                dont_flag = True
                if do_index > -1:
                    sum += multiply(exp)
                    dont_flag = False
            elif do_index > -1:
                sum += multiply(exp)
                dont_flag = False
            else:
                if not dont_flag:
                    sum += multiply(exp)

            expressions.remove(exp)
            start_index = exp_index
        print(sum)


# part1("input")
part2("input")
