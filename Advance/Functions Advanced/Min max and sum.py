def min_max_sum(nums):
    min_number = [f'The minimum number is {min(nums)}']
    max_number = [f'The maximum number is {max(nums)}']
    sum_number = [f'The sum number is: {sum(nums)}']
    return min_number + max_number + sum_number

numbers = list(map(int, input().split()))
print(*[el for el in min_max_sum(numbers)], sep='\n')

