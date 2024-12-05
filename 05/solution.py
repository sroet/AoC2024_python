import argparse
import time


def read_file(fname):
    data = []
    rules = []
    updates = []
    with open(fname, "r") as file:
        section_2 = False
        for line in file:
            strip = line.strip()
            if strip != "":
                if not section_2:
                    rules.append(tuple(int(i) for i in strip.split("|")))
                else:
                    updates.append([int(i) for i in strip.split(",")])
            else:
                section_2 = True
    return rules, updates


def fix_order(update, after_dict):
    options = set(update)
    temp = [(len(options & after_dict.get(i, set())), i) for i in options]
    temp.sort(reverse=True)
    return [i for _, i in temp]


def parts(data):
    rules, updates = data
    out_1 = 0
    out_2 = 0
    after_dict = {}
    for i, j in rules:
        nb = after_dict.get(i, set())
        after_dict[i] = nb | {j}
    for update in updates:
        for i, item in enumerate(update[:-1]):
            if any((item in after_dict.get(j, {})) for j in update[i + 1 :]):
                out_2 += fix_order(update, after_dict)[len(update) // 2]
                break
        else:
            out_1 += update[len(update) // 2]
    return out_1, out_2


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1, total_2 = parts(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Part 2: {total_2}")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
