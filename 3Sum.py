#3Sum


#can't solve problem (time out)
def Sum3_brute_force(l):
    result = []
    l.sort()

    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue
        for j in range(i+1, len(l)-1):
            if j > i+1 and l[j] == l[j-1]:
                continue
            for k in range(j+1, len(l)):
                if k>j+1 and l[k] == l[k-1]:
                    continue

                if l[i] + l[j] + l[k] == 0:
                    result.append([l[i], l[j], l[k]])

    return result

nums = [-1, 0, 1, 2, -1 ,-4]
print(Sum3_brute_force(nums))


def Sum3_two_pointers(nums):
    results =[]
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
    return results
print(Sum3_two_pointers(nums))