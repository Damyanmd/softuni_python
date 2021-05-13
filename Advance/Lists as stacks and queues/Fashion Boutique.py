from collections import deque
clothes = deque(map(int, input().split(' ')))
rack = int(input())
count_racks = 1
used_rack = rack
while True:
    if len(clothes) == 0:
        break
    if clothes[0] <= used_rack:
        used_rack -= clothes[0]
        clothes.popleft()
    elif clothes[0] > used_rack:
        used_rack = rack
        count_racks += 1
print(count_racks)