from collections import deque
price_per_bullet = int(input())
gun_barrel = int(input())
bullets = list(map(int, input().split(' ')))
locks = deque(map(int, input().split(' ')))
value_intelligence = int(input())
shoot_bullets = 0
while True:
    for bullet in range(gun_barrel):
        if len(locks) == 0:
            break
        elif len(bullets) == 0:
            break
        lock = locks[0]
        lock -= bullets.pop()
        shoot_bullets += 1
        if lock >= 0:
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')
    if len(bullets) > 0:
        print('Reloading!')
    if len(locks) == 0:
        print(f'{len(bullets)} bullets left. Earned ${value_intelligence - (shoot_bullets * price_per_bullet)}')
        break
    elif len(bullets) == 0:
        print(f'Couldn\'t get through. Locks left: {len(locks)}')
        break