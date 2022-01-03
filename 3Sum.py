#3Sum


#can't solve problem (time out)
def Sum3(l):
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
print(Sum3(nums))