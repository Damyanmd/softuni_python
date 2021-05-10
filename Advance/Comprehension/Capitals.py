from collections import deque
countries = input().split(', ')
cities = deque(input().split(', '))
[print(f'{country} -> {cities.popleft()}') for country in countries]