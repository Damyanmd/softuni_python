numbers = list(map(int, input().split(', ')))
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []
[positive_numbers.append(number) if number >= 0 else negative_numbers.append(number) for number in numbers]
[even_numbers.append(number) if number % 2 == 0 else odd_numbers.append(number) for number in numbers]
print(f'Positive: {", ".join(str(x) for x in positive_numbers)}')
print(f'Negative: {", ".join(str(x) for x in negative_numbers)}')
print(f'Even: {", ".join(str(x) for x in even_numbers)}')
print(f'Odd: {", ".join(str(x) for x in odd_numbers)}')