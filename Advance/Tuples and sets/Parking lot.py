n = int(input())
cars_in = []
for i in range(n):
    data = input()
    command, car = data.split(', ')
    if command == 'IN':
        cars_in.append(car)
    elif command == 'OUT':
        cars_in.remove(car)
if len(cars_in) == 0:
    print('Parking Lot is Empty')
else:
    print('\n'.join(set(cars_in)))