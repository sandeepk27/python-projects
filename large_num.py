nums = [0, 0, 0, 1, 1, -1, 2, 3, 5, 7, -2]


def largest_number(nums):
    i = 0
    nums.sort(reverse=True)

    if len(nums) == 1:
        return None
    if nums[i] == nums[i+1]:
        return largest_number(nums[i+1:])
    elif nums[i] > nums[i+1]:
        return nums[i]


print(largest_number(nums))
