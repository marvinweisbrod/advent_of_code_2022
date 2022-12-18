import helpers

helper_array = ("A", "B", "C", "A", "B", "C")


# result as 0 = draw, -1 = we lost, 1 = we won
def rps_result(first, second):
    if first == second:
        return 0
    if (first == "A" and second == "B") or (first == "B" and second == "C") or (first == "C" and second == "A"):
        return 1
    if (second == "A" and first == "B") or (second == "B" and first == "C") or (second == "C" and first == "A"):
        return -1
    print(round)

def rps_points_from_result(result):
    if result == -1:
        return 0
    if result == 0:
        return 3
    if result == 1:
        return 6
    print(result)


def get_symbol_score(symbol):
    return ord(symbol)-64


def result_and_enemy_to_symbol(result, enemy):
    if result == 0:
        return enemy
    enemy_idx = ord(enemy)-65
    if result == 1:
        return helper_array[enemy_idx+1]
    if result == -1:
        return helper_array[enemy_idx+2]


def calc_score_part1(round):
    my_play = chr(ord(round[1])-23)
    result = rps_result(round[0], my_play)
    points = rps_points_from_result(result) + get_symbol_score(my_play)
    return points


def calc_score_part2(round):
    required_result = ord(round[1])-89
    required_symbol = result_and_enemy_to_symbol(required_result, round[0])
    return rps_points_from_result(required_result) + get_symbol_score(required_symbol)


def main():
    lines = helpers.read_resource_as_lines("day_02.txt")
    rounds = []
    for line in lines:
        rounds.append(line.split())
    
    my_total = 0
    for round in rounds:
        my_total += calc_score_part1(round)
    print("Part 1: My score would be: " + str(my_total))

    my_total = 0
    for round in rounds:
        my_total += calc_score_part2(round)
    print("Part 2: My score would be: " + str(my_total))
    

main()