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
    return data[0]


def part_1(data):
    data = deque((i, e) for i, e in enumerate(data))
    start = 0
    out = 0
    while data:
        i, left = data.popleft()
        if i % 2 == 0:
            # datablock
            temp = i // 2
            for _ in range(left):
                out += start * temp
                start += 1
        else:
            j = 1
            while j % 2 == 1 and data:
                j, right = data.pop()
            if j % 2 == 1:
                # No data blocks left
                break
            temp = j // 2
            if right <= left:
                # less data than empty space
                for _ in range(right):
                    out += start * temp
                    start += 1
                left -= right
                if left > 0:
                    data.appendleft((i, left))
            else:
                # more data than empty space
                for _ in range(left):
                    out += start * temp
                    start += 1
                right -= left
                if right > 0:
                    data.append((j, right))
    return out


def part_2(data):
    data = deque((i, e) for i, e in enumerate(data))
    start = 0
    out = 0
    while data:
        i, left = data.popleft()
        if i % 2 == 0:
            # datablock
            temp = i // 2
            for _ in range(left):
                out += start * temp
                start += 1
        else:
            j = 1
            right = 0
            temp = []
            while (j % 2 == 1 or right > left) and data:
                j, right = data.pop()
                temp.append((j, right))
            # force last item to be a (new) empty space
            if j % 2 == 1 or right > left:
                # No data blocks fit
                start += left
                data.extend(temp[::-1])
                continue
            else:
                temp[-1] = (-1, temp[-1][1])
                data.extend(temp[::-1])
            temp = j // 2
            if right <= left:
                # less data than empty space
                for _ in range(right):
                    out += start * temp
                    start += 1
                left -= right
                if left > 0:
                    data.appendleft((i, left))
            else:
                print(f"{left=}, {i=}, {right=}, {j=}")
                raise ValueError()
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
