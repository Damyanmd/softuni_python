from collections import deque
food = int(input())
orders = deque(map(int, input().split(' ')))
print(max(orders))
while True:
    if len(orders) == 0:
        break
    if food >= orders[0]:
        food -= orders[0]
        orders.popleft()
    else:
        break
if len(orders) == 0:
    print('Orders complete')
else:
    reversed(orders)
    print(f'Orders left: {" ".join(str(x) for x in orders)}')