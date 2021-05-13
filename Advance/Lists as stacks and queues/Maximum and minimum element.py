n = int(input())
stack = []
for i in range(n):
    data = input().split(' ')
    command = data[0]
    if command == '1':
        number = int(data[1])
        stack.append(number)
    elif command == '2':
        if stack == []:
            continue
        else:
            stack.pop()
    elif command == '3':
        if stack == []:
            continue
        print(max(stack))
    elif command == '4':
        if stack == []:
            continue
        print(min(stack))
new_stack = []
for i in range(len(stack)):
    new_stack.append(stack.pop())

print(", ".join(str(x) for x in new_stack))

