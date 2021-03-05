def negative_positive(nums):
    negative_numbers = list(filter(lambda x: x < 0, nums))
    print(sum(negative_numbers))
    positive_numbers = list(filter(lambda x: x > 0, nums))
    print(sum(positive_numbers))
    if abs(sum(negative_numbers)) > sum(positive_numbers):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')

numbers = list(map(int, input().split()))
negative_positive(numbers)