import argparse
import time
import itertools as itt


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    return data


def convert_map(complete_map):
    out = {}
    max_y = len(complete_map)
    max_x = len(complete_map[0])
    for y, row in enumerate(complete_map):
        for x, c in enumerate(row):
            if c != ".":
                temp = out.get(c, set())
                temp.add(complex(x, y))
                out[c] = temp
    return out, (max_x, max_y)


def part_1(data):
    coordinates = set()
    data, (max_x, max_y) = convert_map(data)
    for values in data.values():
        for val1, val2 in itt.combinations(values, 2):
            diff = val2 - val1
            for temp in [val2 + diff, val1 - diff]:
                x, y = temp.real, temp.imag
                if 0 <= x < max_x and 0 <= y < max_y:
                    coordinates.add(temp)
    return len(coordinates)


def part_2(data):
    coordinates = set()
    data, (max_x, max_y) = convert_map(data)
    for values in data.values():
        for val1, val2 in itt.combinations(values, 2):
            diff = val2 - val1
            temp = val1
            while 0 <= temp.real < max_x and 0 <= temp.imag < max_y:
                coordinates.add(temp)
                temp += diff
            temp = val1
            while 0 <= temp.real < max_x and 0 <= temp.imag < max_y:
                coordinates.add(temp)
                temp -= diff
    return len(coordinates)


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
