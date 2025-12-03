import argparse
import time
import re
from collections import Counter

def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                _, px, py, _, vx, vy = re.split(' |=|,', strip)
                p = complex(int(px), int(py))
                v = complex(int(vx), int(vy))
                data.append((p, v))
    return data


def part_1(data):
    steps = 100
    #gridx, gridy = 11, 7 # example grid
    gridx, gridy = 101, 103
    robots = set(data)
    for _ in range(steps):
        robots = do_step(robots, (gridx, gridy))
    q1, q2, q3, q4 = 0, 0, 0, 0
    for p, _ in robots:
        px, py = p.real, p.imag
        if px < gridx//2:
            if py < gridy//2:
                q1 += 1
            if py > gridy//2:
                q2 += 1
        if px > gridx//2:
            if py < gridy//2:
                q3 += 1
            if py > gridy//2:
                q4 += 1
    out = q1 * q2 * q3 * q4
    return(out)

def do_step(robots, grid):
    gridx, gridy = grid    
    new_set = set()
    while robots:
        p, v = robots.pop()
        p += v
        px, py = p.real, p.imag
        px %= gridx
        py %= gridy
        p = complex(px,py)
        new_set.add((p, v))
    return new_set


def print_grid(robots, grid):
    positions = set(p for p,_ in robots)
    gridx, gridy = grid
    for y in range(gridy):
        print(''.join(["#" if complex(x, y) in positions else " " for x in range(gridx)]))
            

def part_2(data):
    grid = 101, 103
    robots = set(data)
    out = 0
    count = 0
    while True:
        out += 1
        robots = do_step(robots, grid)
        xs = Counter(i.real for i, _ in robots)
        ys = Counter(i.imag for i, _ in robots)
        _, max_y = ys.most_common(1)[0]
        _, max_x = xs.most_common(1)[0]
        if max_y > 31 and max_x > 25:
            print_grid(robots, grid)
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
