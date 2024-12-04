import argparse
import time
import re


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    return data


def part_1(data):
    # match literal "mul(", any numer digits
    # literal ",", any number digits, literal ")"
    # use groups to pull out the numbers
    patern = r"mul\((\d+),(\d+)\)"
    out = 0
    for row in data:
        for match in re.finditer(patern, row):
            a, b = match.group(1, 2)
            out += int(a) * int(b)
    return out


def part_2(data):
    # match part 1 or match the
    # 'do()' 'don't()' literals
    patern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    out = 0
    enabled = True
    for row in data:
        for match in re.finditer(patern, row):
            if match[0] == "do()":
                enabled = True
            elif match[0] == "don't()":
                enabled = False
            elif enabled:
                a, b = match.group(1, 2)
                out += int(a) * int(b)
    return out


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1 = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2(data)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
