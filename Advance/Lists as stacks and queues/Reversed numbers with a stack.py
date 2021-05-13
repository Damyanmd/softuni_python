text = input().split(' ')
stack = []

for i in range(len(text)):

    stack.append(text.pop())

print(" ".join(stack))