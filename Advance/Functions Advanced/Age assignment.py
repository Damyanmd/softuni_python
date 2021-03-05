def age_assignment(*args, **kwargs):
    list_args = list(args)
    new_dict = {}
    for key, value in kwargs.items():
        for word in list_args:
            if word[0] == key:
                new_dict[word] = value
                continue

    return new_dict

print(age_assignment('Peter', 'George', G=26, P=19))