def arrayPairSum(nums):
    nums.sort()

    pair_count =0
    sum = 0
    while pair_count < len(nums):
        pair = [nums[pair_count], nums[pair_count+1]]
        sum += min(pair)
        pair_count += 2

    return sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))

def arrayPairSum_2(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) ==2:
            sum += min(pair)
            pair = []

    return sum

print(arrayPairSum_2(nums))

def arrayPairSum_3(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum

print(arrayPairSum_3(nums))
def arrayPairSum_4(nums):
    return sum(sorted(nums)[::2])

print(arrayPairSum_4(nums))