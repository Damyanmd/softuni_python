def odd_even(command, nums):
    if command == 'Even':
        result = list(filter(lambda x: x % 2 == 0, nums))
        return sum(result) * len(nums)
    else:
        result = list(filter(lambda x: x % 2 != 0, nums))
        return sum(result) * len(nums)

command = input()
numbers = list(map(int, input().split()))
print(odd_even(command, numbers))