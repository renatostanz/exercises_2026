missing_chars = 'IEHOVA#'

def indiana_path(field, length, width, current_position, directions, missing_chars_marker):
    if missing_chars_marker == 7:
        return directions

    left_position, right_position, forth_position = [None for i in range(3)]
    if current_position[1] > 0:
        left_position = [current_position[0], current_position[1] - 1]

    if current_position[1] < width - 1:
        right_position = [current_position[0], current_position[1] + 1]

    if current_position[0] > 0:
        forth_position = [current_position[0] - 1, current_position[1]]


    next_char = missing_chars[missing_chars_marker]
    if left_position and next_char == field[left_position[0]][left_position[1]]:
        directions.append("left"), 
        answer = indiana_path(
                field, 
                length, 
                width, 
                left_position, 
                directions, 
                missing_chars_marker + 1
        )
        if len(answer) == 7:
            return directions
        else:
            directions.pop()

    if right_position and next_char == field[right_position[0]][right_position[1]]:
        directions.append("right")
        answer = indiana_path(
                field, 
                length, 
                width, 
                right_position, 
                directions, 
                missing_chars_marker + 1
        )
        if len(answer) == 7:
            return directions
        else:
            directions.pop()

    if forth_position and next_char == field[forth_position[0]][forth_position[1]]:
        directions.append("forth"), 
        answer = indiana_path(
                field, 
                length, 
                width, 
                forth_position, 
                directions,
                missing_chars_marker + 1
        )
        if len(answer) == 7:
            return directions
        else:
            directions.pop()

    return directions
                                                    


def get_field(length, width):
    fields_with_strings = [input() for i in range(length)]
    return [list(string) for string in fields_with_strings]


def find_first_position(line):
    for i, char in enumerate(line):
        if char == '@':
            return i

    raise ValueError("No @ found")


def play():
    number_of_rounds = int(input())
    for i in range(number_of_rounds):
        length_and_width = input()
        length, width = [int(i) for i in length_and_width.split()]
        field = get_field(length, width)
        first_position = find_first_position(field[-1])
        answer = indiana_path(field, length, width, [length - 1, first_position], [], 0)
        print(' '.join(answer))


play()
