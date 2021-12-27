#Two_Sum.py

"""
입력 :
nums = [2,7, 11, 15], target = 9

출력 :
[0, 1]
"""
nums = [2,7, 11, 15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum_2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

def twoSum_3(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return[i, nums_map[target - num]]