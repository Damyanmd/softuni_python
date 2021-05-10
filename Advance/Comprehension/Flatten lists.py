input_list = [new_list.split() for new_list in input().split('|')]

new_list = [element for list in reversed(input_list) for element in list]
print(' '.join(new_list))