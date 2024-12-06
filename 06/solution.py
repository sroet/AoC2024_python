import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    return data


def turn_right(direction):
    return complex(direction.imag, -direction.real)


def part_1(data):
    max_y = len(data)
    max_x = len(data[0])
    obstacles = {
        complex(y, x)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "#"
    }
    place = [
        complex(y, x)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "^"
    ][0]
    direction = complex(-1, 0)
    visited = set()
    while 0 <= place.real < max_y and 0 <= place.imag < max_x:
        visited.add(place)
        while place + direction in obstacles:
            direction = turn_right(direction)
        place += direction
    return len(visited), visited


def part_2(data):
    # Can't get this quick enough now
    pass


def check_for_loops(data, extra_obstacle):
    max_y = len(data)
    max_x = len(data[0])
    obstacles = {
        complex(y, x)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "#"
    }
    obstacles = obstacles | set([extra_obstacle])
    place = [
        complex(y, x)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "^"
    ][0]
    direction = complex(-1, 0)
    visited = set()
    while 0 <= place.real < max_y and 0 <= place.imag < max_x:
        if (place, direction) in visited:
            return True
        visited.add((place, direction))
        while place + direction in obstacles:
            direction = turn_right(direction)
        place += direction
    return False


def part_2_brute_force(data, visited):
    max_y = len(data)
    max_x = len(data[0])
    out = 0
    obstacles = {
        complex(y, x)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "#"
    }
    for obstacle in visited:
        out += int(check_for_loops(data, obstacle))
    return out


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1, visited = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2_brute_force(data, visited)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
