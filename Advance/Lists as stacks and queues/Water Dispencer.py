from collections import deque
quantity = int(input())
people = input()
list_people = deque()
while people != 'Start':
    list_people.append(people)
    people = input()
command = input()
while command != 'End':
    if command.isdigit():
        liters = int(command)
        if liters <= quantity:
            quantity -= liters
            print(f'{list_people.popleft()} got water')
        else:
            print(f'{list_people.popleft()} must wait')
    else:
        command, liters = command.split(' ')
        quantity += int(liters)
    command = input()
print(f'{quantity} liters left')