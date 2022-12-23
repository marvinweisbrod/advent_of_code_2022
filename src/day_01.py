import helpers


def main():
    lines = helpers.read_resource_as_lines("day_01.txt")

    # split the file into a list of elves with a sublist of their calories each
    elves=[]
    current_elf_inventory = []
    for line in lines:
        if str.isspace(line):
            elves.append(current_elf_inventory)
            current_elf_inventory = []
            continue

        current_elf_inventory.append(int(line))

    if current_elf_inventory:
        elves.append(current_elf_inventory)

    # creating a dict with their sums so I can sort it while preserving the original indices
    elves_total_cals = {}
    for i in range(len(elves)):
        curr_sum = sum(elves[i])
        elves_total_cals[i] = curr_sum

    elves_total_cals = dict(reversed(sorted(elves_total_cals.items(), key=lambda item: item[1])))

    # tadaa. sorted ranking. not as elegant as I'd have liked
    ranking = list(elves_total_cals.keys())

    print("Most well endowed elf: Number " + str(ranking[0]+1) + ". Calories in his pocket: " + str(elves_total_cals[ranking[0]]))

    # part 2
    top_3_sum = 0
    for i in range(3):
        top_3_sum += elves_total_cals[ranking[i]]

    print("Calories of top 3: " + str(top_3_sum))


if __name__ == "__main__":
    main()