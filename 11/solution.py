import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([int(i) for i in strip.split()])
    return data


def part_1(data):
    state = {}
    for i in data[0]:
        state[i] = state.get(i, 0) + 1
    for _ in range(25):
        new_state = {}
        for key, val in state.items():
            if key == 0:
                new_state[1] = new_state.get(1, 0) + val
            elif len(str(key)) % 2 == 0:
                key = str(key)
                key1 = int(key[: len(key) // 2])
                key2 = int(key[len(key) // 2 :])
                new_state[key1] = new_state.get(key1, 0) + val
                new_state[key2] = new_state.get(key2, 0) + val
            else:
                key *= 2024
                new_state[key] = new_state.get(key, 0) + val
        state = new_state
    return sum(state.values())


def part_2(data):
    state = {}
    for i in data[0]:
        state[i] = state.get(i, 0) + 1
    for _ in range(75):
        new_state = {}
        for key, val in state.items():
            if key == 0:
                new_state[1] = new_state.get(1, 0) + val
            elif len(str(key)) % 2 == 0:
                key = str(key)
                key1 = int(key[: len(key) // 2])
                key2 = int(key[len(key) // 2 :])
                new_state[key1] = new_state.get(key1, 0) + val
                new_state[key2] = new_state.get(key2, 0) + val
            else:
                key *= 2024
                new_state[key] = new_state.get(key, 0) + val
        state = new_state
    return sum(state.values())


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
