# Given an array of ints length 3, return the sum of all the elements.


def sum3(nums):
    solution = 0
    for i in range(len(nums)):
        solution = nums[i] + solution

    return solution


# practice_data_list = [3, 2, 1]
# show = sum3(practice_data_list)
#
# print(show)


# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist,
# returning 0 if the array is length 0.
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]


# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing
# their middle elements.
def middle_way(a, b):
    var_a = a[1]
    var_b = b[1]
    list_of_two_middle_vars = [var_a, var_b]
    return list_of_two_middle_vars


test_list = [[1, 2, 3], [4, 5, 6]]
new_list = middle_way([1, 2, 3], [4, 5, 6])
print(new_list)


# Given an array of ints, return a new array length 2 containing the first and
# last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
    if len(nums) == 1:
        return_array = nums
        return_array.append(nums[0])
        return return_array
    else:
        return_array = [nums[0], nums[len(nums)-1]]
        return return_array



