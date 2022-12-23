import helpers


def is_one_fully_contained(first, second):
    if first[0] <= second[0] and first[1] >= second[1]:
        return True
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    return False


def are_overlapping(first, second):
    if is_one_fully_contained(first, second):
        return True
    if first[0] >= second[0] and first[0] <= second[1]:
        return True
    if first[1] >= second[0] and first[1] <= second[1]:
        return True
    return False


def main():
    lines = helpers.read_resource_as_lines("day_04.txt")

    range_pairs = []
    for line in lines:
        ranges = line.split(",")
        range_a = ranges[0].split("-")
        range_b = ranges[1].split("-")
        range_pairs.append( ( (int(range_a[0]), int(range_a[1])) , (int(range_b[0]), int(range_b[1]))) )

    # part 1
    fully_contained_count = 0
    for pair in range_pairs:
        if is_one_fully_contained(pair[0], pair[1]):
            fully_contained_count += 1

    print("Part 1 - Fully contained ranges: " + str(fully_contained_count))

    # part 2
    overlap_count = 0
    for pair in range_pairs:
        if are_overlapping(pair[0], pair[1]):
            overlap_count += 1

    print("Part 2 - Overlapping ranges: " + str(overlap_count))


if __name__ == "__main__":
    main()