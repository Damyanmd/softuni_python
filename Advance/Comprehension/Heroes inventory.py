people = input().split(', ')
heroes = {name: {} for name in people}

data = input()
while data != 'End':
    name, item, cost = data.split('-')
    if not heroes.get(name):
        heroes[name] = {}
    if not heroes[name].get(item):
        heroes[name].update({item: int(cost)})
    data = input()

print(*[f'{name} -> Items: {len(value)}, Cost: {sum([cost for item, cost in value.items()])}' for name, value in heroes.items()], sep='\n')
