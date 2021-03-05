def even_numbers(nums):
    result = list(filter(lambda x: x % 2 == 0, nums))
    return result


numbers = list(map(int, input().split()))
print(even_numbers(numbers))