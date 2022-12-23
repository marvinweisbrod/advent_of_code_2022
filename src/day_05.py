import helpers


def setup_stacks(lines):
    stacks = []
    for i in range(9):
        stacks.append([])

    setup = []
    for line in lines:
        if line[0] == "[":
            setup.append(line)
        else:
            break
    setup.reverse()

    for line in setup:
        for i in range((len(line)+1)//4):
            character = line[(i*4)+1]
            if not character.isspace():
                stacks[i].append(character)
    return stacks


def main():
    lines = helpers.read_resource_as_lines("day_05.txt")


    # part 1
    stacks = setup_stacks(lines)

    for line in lines:
        if line[0] == "m":
            segments = line.split()
            to_move = int(segments[1])
            origin = int(segments[3])-1
            target = int(segments[5])-1
            for i in range(to_move):
                element = stacks[origin].pop()
                stacks[target].append(element)

    top_crates = ""
    for stack in stacks:
        top_crates += stack[len(stack)-1]

    print(stacks)
    print("The top crates are: " + str(top_crates))

    # part 2

    stacks = setup_stacks(lines)

    for line in lines:
        if line[0] == "m":
            segments = line.split()
            to_move = int(segments[1])
            origin = int(segments[3])-1
            target = int(segments[5])-1
            temp_stack = []
            for i in range(to_move):
                temp_stack.append(stacks[origin].pop())
            temp_stack.reverse()
            for element in temp_stack:
                stacks[target].append(element)

    top_crates = ""
    for stack in stacks:
        top_crates += stack[len(stack)-1]

    print(stacks)
    print("The top crates are: " + str(top_crates))


if __name__ == "__main__":
    main()