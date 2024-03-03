def get_next_position(position, direction_mapper, direction, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    desired_row_index = (desired_row_index + len(matrix)) % len(matrix)
    desired_col_index = (desired_col_index + len(matrix)) % len(matrix)

    return desired_row_index, desired_col_index



def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


n = int(input())

matrix = []
current_pos = None
enemy_counter = 0
armor = 300
hits = 0

map_direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row_index in range(n):
    line = list(input())

    if 'J' in line:
        current_col = line.index('J')
        current_pos = [row_index, current_col]
    if 'E' in line:
        enemy_counter += line.count("E")

    matrix.append(line)

while enemy_counter > 0 and armor > 0:
    command = input()

    current_row_index, current_col_index = current_pos
    next_row_index,next_col_index = get_next_position(current_pos,map_direction,command,matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = 'J'
    matrix[current_row_index][current_col_index] = "-"
    current_pos = [next_row_index, next_col_index]

    if symbol == "E":
        matrix[current_row_index][current_col_index] = "-"
        if enemy_counter == 1:
            print("Mission accomplished, you neutralized the aerial threat!")
            print_matrix(matrix)
            exit()
        armor -= 100
        hits += 1
        enemy_counter -= 1
        if armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{current_pos[0]}, {current_pos[1]}]!")
            print_matrix(matrix)
            exit()
    elif symbol == "R":
        armor = 300
        matrix[current_row_index][current_col_index] = "-"

if hits == 3:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{current_pos[0]}, {current_pos[1]}]!")

print_matrix(matrix)