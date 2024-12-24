import argparse
import time
from collections import deque


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([int(i) for i in strip])
    return data


def part_1(data):
    # find starts
    starts = []
    max_x = len(data[0])
    max_y = len(data)
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == 0:
                starts.append((x, y))
    # do DFS per start
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    out = 0
    for start in starts:
        temp = 0
        x, y = start
        seen = set((start))
        todo = deque([(x, y, 0)])
        while todo:
            x, y, v = todo.popleft()
            if v == 9:
                temp += 1
                continue
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < max_x and 0 <= ny < max_y):
                    continue
                if (nx, ny) in seen:
                    continue
                if data[ny][nx] == v + 1:
                    seen.add((nx, ny))
                    todo.appendleft((nx, ny, v + 1))
        out += temp
    return out


def part_2(data):
    # find starts
    starts = []
    max_x = len(data[0])
    max_y = len(data)
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == 0:
                starts.append((x, y))
    # do DFS per start
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    out = 0
    for start in starts:
        temp = 0
        x, y = start
        seen = set((start))
        todo = deque([(x, y, 0)])
        while todo:
            x, y, v = todo.popleft()
            if v == 9:
                temp += 1
                continue
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < max_x and 0 <= ny < max_y):
                    continue
                # if (nx, ny) in seen:
                #    continue
                if data[ny][nx] == v + 1:
                    seen.add((nx, ny))
                    todo.appendleft((nx, ny, v + 1))
        out += temp
    return out
    pass


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
