# Given an array of ints length 3, return the sum of all the elements.


def sum3(nums):
    solution = 0
    for i in range(len(nums)):
        solution = nums[i] + solution

    return solution


practice_data_list = [3, 2, 1]
show = sum3(practice_data_list)

print(show)
