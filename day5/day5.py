def get_bpasses():
    with open("input.txt", "r") as file:
        bpasses = file.read().splitlines()
    return bpasses


def calculate_id(bpass):
    front, back, left, right = 0, 127, 0, 7
    
    for char in bpass:
        delta_y = (back - front + 1) // 2
        delta_x = (right - left + 1) // 2

        if char == "F": 
            back -= delta_y
        elif char == "B":
            front += delta_y
        elif char == "L":
            right -= delta_x
        elif char == "R":
            left += delta_x
    
    bpass_id = (front * 8) + left
    return bpass_id


def max_bpass_id(bpasses):
    max_bpass_id = 0

    for bpass in bpasses:
        bpass_id = calculate_id(bpass)

        if bpass_id > max_bpass_id:
            max_bpass_id = bpass_id

    return max_bpass_id


def find_missing_id(bpasses):
    seats = [False] * 990

    for bpass in bpasses:
        bpass_id = calculate_id(bpass)
        seats[bpass_id] = True
    
    bpass_id = 989
    for seat_taken in reversed(seats):
        if not seat_taken:
            return bpass_id
        bpass_id -= 1


bpasses = get_bpasses()
print(max_bpass_id(bpasses)) # 989
print(find_missing_id(bpasses)) # 548