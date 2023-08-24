
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n
    print(lis)
    for i in range(1, n):
        for j in range(0, i):
            print(f"a[{i}]={arr[i]} a[{j}]={arr[j]} lis[{i}]={lis[i]} lis[{j}]={lis[j]}")
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                print(f"lis[{i}]={lis[i]}")
    print(lis)
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum

#arr = [3, 4, 2, 8, 10, 5, 1]
arr = [3, 4, 2, 8, 10, 5, 1, 6, 7, 9]
print(longest_increasing_subsequence(arr))
