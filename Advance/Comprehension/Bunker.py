item_categories = input().split(', ')
categories = {category: [] for category in item_categories}
n = int(input())
count_items = 0
quality_items = 0
for _ in range(n):
    items = input().split(' - ')
    quantity, quality = items[2].split(';')
    count_items += int((quantity.split(':'))[1])
    quality_items += int((quality.split(':'))[1])
    categories[items[0]].append(items[1])
print(f'Count of items: {count_items}')
print(f'Average quality: {(quality_items/len(categories)):.2f}')
print(*[f'{name} -> {", ".join(value)}' for name, value in categories.items()], sep='\n')