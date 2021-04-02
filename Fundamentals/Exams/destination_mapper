import re

pattern = r"(/|\=)[A-Z][a-zA-Z][a-zA-Z]+\1"
text = input()

valid_destinations = [d.group() for d in re.finditer(pattern, text)]
for index in range(len(valid_destinations)):
    if valid_destinations[index].startswith("="):
        valid_destinations[index] = valid_destinations[index].strip('=')
    else:
        valid_destinations[index] = valid_destinations[index].strip('/')

travel_points = sum([len(d) for d in valid_destinations])

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
