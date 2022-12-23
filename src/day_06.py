import helpers


def length_til_unique_marker(text, marker_length):
    for i in range(len(text)-marker_length-1):
        potential_marker = text[i:i+marker_length]
        if len(set(potential_marker)) == marker_length:
            print("Found those: " + potential_marker + ". total length til end of marker: " + str(i+marker_length))
            break


def main():
    line = helpers.read_resource_as_lines("day_06.txt")[0]
    length_til_unique_marker(line, 4)
    length_til_unique_marker(line, 14)


if __name__ == "__main__":
    main()