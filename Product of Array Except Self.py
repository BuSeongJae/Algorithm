# 내 풀이/ 오답 : 시간복잡도 O(n^2)
def Product_of_array_except_self(nums):
    results = []
    c = 0
    for i in range(len(nums)):
        product = 1
        n=0
        while n < len(nums):
            if n != c:
                product = product * nums[n]
            n += 1
        c += 1

        results.append(product)
    return results

nums = [-1, 1, 0, -3, 3]
print(Product_of_array_except_self(nums))


#  book answer O(n)
def productExceptSelf(nums):
    out = []
    p = 1
    # left product
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    # product left num and right num
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out

print(productExceptSelf(nums))

