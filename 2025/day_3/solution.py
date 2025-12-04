import itertools

f1 = open('input1.txt', 'r')
i1 = f1.read()
f1.close()
import re
sample = """987654321111111
811111111111119
234234234234278
818181911112111"""

def highest_two_digit_anywhere(sequence):
    digits = [d for d in sequence]
    max_num = None
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            num = int(digits[i] + digits[j])
            if 10 <= num <= 99:
                if max_num is None or num > max_num:
                    max_num = num
    return max_num

def highest_twelve_digit_in_order(sequence):
    digits = [d for d in sequence]
    n = len(digits)
    result = []
    start = 0
    for k in range(12):
        end = n - (12 - (k + 1))
        max_digit = max(digits[start:end])
        idx = digits.index(max_digit, start, end)
        result.append(max_digit)
        start = idx + 1
    return int(''.join(result))

def sol1(input):
    batteries = input.splitlines()
    sum = 0
    for battery in batteries:
        sum += highest_two_digit_anywhere(battery)

    return sum

def sol2(input):
    batteries = input.splitlines()
    sum = 0
    for battery in batteries:
        sum += highest_twelve_digit_in_order(battery)

    return sum

print(sol2(i1))