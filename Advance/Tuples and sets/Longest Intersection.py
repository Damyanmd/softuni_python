def splitting_intersection(unslpit):
    part = unslpit.split(',')
    part = list(map(int, part))
    return part

def longest_length(first, second):
    longest_intersection = []
    beginning = first[0]
    end = first[1]
    if second[0] > beginning:
        beginning = second[0]
    if second[1] < end:
        end = second[1]
    longest_intersection.append(beginning)
    longest_intersection.append(end)
    return longest_intersection

def checker_for_longest_intersection(new_length, previous_length):
    checker = []
    for _ in range(new_length[0], new_length[1] + 1):
        checker.append(_)
    if len(checker) > len(previous_length):
        return checker
    else:
        return previous_length

longest_intersection = []
n = int(input())
for i in range(n):
    intersection = input()
    first_part, second_part = intersection.split('-')
    first_intersection = splitting_intersection(first_part)
    second_intersection = splitting_intersection(second_part)
    length = longest_length(first_intersection, second_intersection)
    longest_intersection = checker_for_longest_intersection(length, longest_intersection)

print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
