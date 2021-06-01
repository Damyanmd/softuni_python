class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, round(size / 2))

    def add_item(self, item_name):
        total_items_count = sum(value for value in self.items.values())
        if total_items_count < self.capacity:
            self.items[item_name] = 1
            return f'{item_name} added to the store'
        else:
            return f'Not enough capacity in the store'

    def remove_item(self, item_name, count):
        try:
            if self.items[item_name] >=count:
                self.items[item_name] -= count
                return f'{count} {item_name} removed from the store'
            else:
                return f'Cannot remove {count} {item_name}'
        except:
            return f'Cannot remove {count} {item_name}'

first_store = Store('First store', 'Fruit and Veg', 20)
second_store = Store.from_size('Second store', 'Clothes', 500)

print(first_store)
print(second_store)

print(first_store.add_item('potato'))
print(second_store.add_item('jeans'))

print(first_store.remove_item('tomatoes', 1))
print(second_store.remove_item('jeans', 1))