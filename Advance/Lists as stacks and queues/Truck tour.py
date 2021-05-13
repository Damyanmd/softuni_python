pump_stations = int(input())
stations = []
finished = False
for i in range(pump_stations):
    stations.append(input())
for station in range(len(stations)):
    petrol, distance = stations[station].split(' ')
    petrol = int(petrol)
    distance = int(distance)
    if petrol >= distance:
        petrol_capacity = petrol - distance
        starting_route = station + 1
        while True:
            if starting_route >= len(stations):
                starting_route = 0
            if starting_route == station:
                finished = True
                print(station)
                break
            petrol, distance = stations[starting_route].split(' ')
            petrol = int(petrol)
            distance = int(distance)
            petrol_capacity = (petrol + petrol_capacity) - distance
            if petrol_capacity < 0:
                break
            else:
                starting_route += 1
    if finished:
        break
