from collections import deque
without_set = deque(sorted(input()))
with_set = deque(sorted(set(without_set)))
while len(with_set) > 0:
    print(f'{with_set[0]}: {without_set.count(with_set.popleft())} time/s')