from collections import deque
green_light = int(input())
free_window = int(input())
data = input()
time_left_free_window = free_window
cars = deque()
pass_through_cars = 0
car = deque()
while data != 'END':
    if data == 'green':
        time_green_light_left = green_light
        while len(cars) > 0:
            if time_green_light_left == 0:
                break
            car = deque(cars[0])
            for i in range(time_green_light_left):
                if len(car) == 0:
                    time_green_light_left -= i
                    cars.popleft()
                    pass_through_cars += 1
                    break
                car.popleft()
            if len(car) > 0:
                time_green_light_left = 0
                for i in range(time_left_free_window):
                    if len(car) == 0:
                        pass_through_cars += 1
                        cars.popleft()
                        break
                    car.popleft()
                if len(car) > 0:
                    print('A crash happened!')
                    print(f'{cars.popleft()} was hit at {car.popleft()}.')
                    break
        if len(car) > 0:
            break
    else:
        cars.append(data)
    data = input()
if data == 'END':
    print('Everyone is safe.')
    print(f'{pass_through_cars} total cars passed the crossroads.')