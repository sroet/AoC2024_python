import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                test, values = strip.split(":")
                data.append((int(test), list(int(i) for i in values.split())))
    return data


def solve_equation(test, values, part2=False):
    if len(values) == 1:
        return values[0] == test
    val = values.pop()
    if val > test:
        return False
    temp_values = values.copy()
    temp_values[-1] *= val
    out = solve_equation(test, temp_values, part2)
    if out:
        return out
    temp_values = values.copy()
    temp_values[-1] += val
    out = solve_equation(test, temp_values, part2)
    if out or not part2:
        return out
    temp_values = values.copy()
    temp_values[-1] = int(str(val) + str(values[-1]))
    return solve_equation(test, temp_values, part2)


def part_1(data):
    out = 0
    false_list = []
    for test, values in data:
        if solve_equation(test, values[::-1].copy()):
            out += test
        else:
            false_list.append((test, values))
    return out, false_list


def part_2(data):
    out = 0
    for test, values in data:
        if solve_equation(test, values[::-1], part2=True):
            out += test
    return out


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1, data = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2(data)
    print(f"Part 2: {total_1+total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
