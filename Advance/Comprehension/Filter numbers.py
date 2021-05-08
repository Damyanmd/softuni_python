start = int(input())
end = int(input())
numbers = [num for num in range(start, end + 1)]
numbers_one_to_ten = [num for num in range(2, 11)]

filtered = [num for num in numbers if any([num % x == 0 for x in numbers_one_to_ten])]
print(filtered)