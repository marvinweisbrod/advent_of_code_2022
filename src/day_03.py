import helpers


def letter_to_prio(letter):
    char_val = ord(letter)
    # A-Z
    if char_val >= 65 and char_val <= 90:
        return char_val - 38
    # rest
    return char_val - 96


def main():
    lines = helpers.read_resource_as_lines("day_03.txt")
    backpacks = []
    for line in lines:
        backpack = []
        backpack.append(line[0:(len(line)//2)])
        backpack.append(line[(len(line)//2):])
        backpacks.append(backpack)


    # part 1
    priority_sum = 0
    for backpack in backpacks:
        for letter in backpack[0]:
            pos = backpack[1].find(letter)
            if pos != -1:
                priority_sum += letter_to_prio(letter)
                break
    
    print("Part 1 Priority Sum: " + str(priority_sum))


    # part 2
    priority_sum = 0
    for i in range(len(lines)//3):
        for letter in lines[i*3]:
            found_in_second = lines[(i*3)+1].find(letter)
            found_in_third = lines[(i*3)+2].find(letter)
            if found_in_second != -1 and found_in_third != -1:
                priority_sum += letter_to_prio(letter)
                break

    print("Part 2 Priority Sum: " + str(priority_sum))


if __name__ == "__main__":
    main()