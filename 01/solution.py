import argparse
import time
from collections import Counter


def read_file(fname):
    left_list = []
    right_list = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                left, right = strip.split()
                left_list.append(int(left))
                right_list.append(int(right))
    return left_list, right_list


def part_1(data):
    left_list, right_list = data
    left_list.sort()
    right_list.sort()
    out = 0
    for l, r in zip(left_list, right_list):
        out += abs(l - r)
    return out


def part_2(data):
    left_list, right_list = data
    count_right = Counter(right_list)
    out = 0
    for l in left_list:
        out += l * count_right[l]
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
