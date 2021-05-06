from collections import deque
n = int(input())
unique_elements = []
for i in range(n):
    element = deque(input().split(' '))
    while len(element) > 0:
        unique_elements.append(element.popleft())


print('\n'.join(set(unique_elements)))