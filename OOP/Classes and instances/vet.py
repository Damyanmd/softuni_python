class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f'{animal_name} registered in the clinic'
        else:
            return f'Not enough space'

    def unregister_animal(self, animal_name):
        filtered_name = [n for n in self.animals if n == animal_name]
        if filtered_name:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f'{animal_name} unregistered successfully'
        else:
            return f'{animal_name} not in the clinic'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'
