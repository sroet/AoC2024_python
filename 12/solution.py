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


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def find_out(data, start, val):
    perimeter = 0
    todo = [start]
    seen = set()
    while todo:
        x, y = todo.pop()
        if (x, y) in seen:
            continue
        if data[y][x] != val:
            perimeter += 1
            continue
        seen.add((x, y))
        for dx, dy in directions:
            if 0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data):
                todo.append((x + dx, y + dy))
            else:
                perimeter += 1
    return len(seen) * perimeter, seen


def find_part_2(data, start, val):
    todo = [start]
    seen = set()
    sides = set()
    while todo:
        x, y = todo.pop()
        if (x, y) in seen:
            continue
        if data[y][x] != val:
            sides.add((x, y))
            continue
        seen.add((x, y))
        for dx, dy in directions:
            if 0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data):
                todo.append((x + dx, y + dy))
            else:
                sides.add((x + dx, y + dy))
    # now group the sides by wether they are left/right sides or up/down sides
    l_sides = set()
    r_sides = set()
    u_sides = set()
    d_sides = set()
    for x, y in sides:
        for (dx, dy), temp in zip(directions, [r_sides, l_sides, d_sides, u_sides]):
            if (x + dx, y + dy) in seen:
                temp.add((x, y))
    sides = 0
    for temp, temp_directions in zip(
        [l_sides, r_sides, u_sides, d_sides],
        [directions[2:], directions[2:], directions[:2], directions[:2]],
    ):
        while temp:
            x, y = temp.pop()
            sides += 1
            for dx, dy in temp_directions:
                temp_x, temp_y = x + dx, y + dy
                while (temp_x, temp_y) in temp:
                    temp.discard((temp_x, temp_y))
                    temp_x += dx
                    temp_y += dy

    return len(seen) * sides, seen


def part_1(data):
    seen = set()
    out = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) not in seen:
                val = data[y][x]
                add, add_seen = find_out(data, (x, y), val)
                out += add
                seen |= add_seen

    return out


def part_2(data):
    seen = set()
    out = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) not in seen:
                val = data[y][x]
                add, add_seen = find_part_2(data, (x, y), val)
                out += add
                seen |= add_seen

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
