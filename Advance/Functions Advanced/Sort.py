def even_numbers(nums):
    result = list(sorted(nums))
    return result


numbers = list(map(int, input().split()))
print(even_numbers(numbers))