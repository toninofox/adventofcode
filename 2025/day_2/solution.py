f1 = open('input1.txt', 'r')
i1 = f1.read()
f1.close()
import re
sample = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def has_repeated_sequence(value):
    s = str(value)
    half_point = len(s) // 2
    return s[:half_point] == s[half_point:]

def has_multiple_repeated_sequence(value):
    pattern =  r'^(\d+?)\1+$'
    matched = re.match(pattern, str(value))
    return matched

def can_be_split_in_half(value):
    s = str(value)
    length = len(s)
    return length % 2 == 0

def sol1(input):
    ranges = input.split(',')
    sum = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in filter(can_be_split_in_half, range(start, end + 1)):
            if has_repeated_sequence(num):
                sum += num

    return sum

def sol2(input):
    ranges = input.split(',')
    sum = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if has_multiple_repeated_sequence(num):
                sum += num

    return sum

print(sol2(i1))