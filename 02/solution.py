import argparse
import time
from itertools import pairwise

def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([int(i) for i in strip.split()])
    return data

def is_safe(report, part_2=False):
    line = 0
    for pos, (i,j) in enumerate(pairwise(report)):
        diff = i-j
        if 1 <= abs(diff) <= 3 and line*diff >= 0:
            line = diff
        else:
            if not part_2:
                return False
            # part_2 or second try in part 2
            temp1 = report.copy()
            temp1.pop(pos)
            temp2 = report.copy()
            temp2.pop(pos+1)
            safe = (is_safe(temp1) or is_safe(temp2))
            if line*diff < 0:
                # problem might be 1 further back
                temp3 = report.copy()
                temp3.pop(pos-1)
                safe = (safe or is_safe(temp3))
            return safe
    else:
        return True
 

def part_1(data):
    safe = 0
    for report in data:
        if is_safe(report):
            safe += 1
    return safe

def part_2(data):
    safe = 0
    for report in data:
        if is_safe(report, part_2=True):
            safe += 1
    return safe

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
