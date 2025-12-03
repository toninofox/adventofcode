f1 = open('input1.txt', 'r')
i1 = f1.read()
f1.close()
import math
sample = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def sol1(instructions):
    current_point = 50
    count = 0
    for instruction in instructions.splitlines():
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == 'L':
            current_point -= distance
        elif turn == 'R':
            current_point +=  distance
        current_point = current_point % 100
        print(instruction,current_point)
        if current_point == 0:
            count += 1

    return count

def sol2 (instructions):
    current_point = 50
    count = 0
    clicks = 0
    for instruction in instructions.splitlines():
        prev_point = current_point
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == 'L':
            final_point = current_point - distance
            multiple_rotations = (current_point != 0 and final_point < 0) or (current_point == 0 and distance >= 100)
            if multiple_rotations:
                if distance >= 100:
                    clicks += current_point == 0 and int(distance // 100) or math.ceil((distance - current_point) / 100)
                else:
                    clicks += 1
            current_point = final_point
        elif turn == 'R':
            final_point = current_point + distance
            if final_point >= 100:
                if distance >= 100:
                    clicks += current_point == 0 and int(distance // 100) or math.floor((distance + current_point) / 100)
                else:
                    clicks += 1
            if final_point % 100 == 0:
                clicks -= 1 # Adjust for landing exactly on 0
            current_point = final_point

        current_point = current_point % 100
        if current_point == 0:
            count += 1
        print(prev_point,instruction, "->",current_point, "clicks:",clicks, "end rotations:",count)

    return count + clicks

print(sol1(i1))