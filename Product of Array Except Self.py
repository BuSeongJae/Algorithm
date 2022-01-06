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

