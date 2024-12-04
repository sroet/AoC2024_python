import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([i for i in strip])
    return data


directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def part_1(data):
    xmas = 0
    for y, row in enumerate(data):
        for x, letter in enumerate(row):
            if letter != "X":
                continue
            for dy, dx in directions:
                temp_y, temp_x = y, x
                for val in "MAS":
                    temp_y += dy
                    temp_x += dx
                    if temp_y < 0 or temp_y >= len(data):
                        break
                    if temp_x < 0 or temp_x >= len(row):
                        break
                    if data[temp_y][temp_x] != val:
                        break
                else:
                    xmas += 1
    return xmas


def part_2(data):
    diags = [(1, 1), (1, -1)]
    xmas = 0
    for y, row in enumerate(data):
        for x, letter in enumerate(row):
            if letter != "A":
                continue
            for dy, dx in diags:
                if y - dy < 0 or y + dy >= len(data):
                    break
                if x + dx < 0 or x + dx >= len(row) or x - dx < 0 or x - dx >= len(row):
                    break
                if data[y + dy][x + dx] + data[y - dy][x - dx] not in ["MS", "SM"]:
                    break
            else:
                xmas += 1
    return xmas


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
