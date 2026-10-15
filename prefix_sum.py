def prefix_sum(arr:list[int]) -> list[int]:
    n: int = len(arr)
    if n == 0:
        return []

    prefix_list = [0] * n # initialize list of length n with zeros
    prefix_list[0] = arr[0]

    i = 1
    while True:
        if i >= n:
            break
        prefix_list[i] = prefix_list[i - 1] + arr[i]
        i += 1
    return prefix_list

arr = [10, 20, 30, 40, 50]
result = prefix_sum(arr)
for i in range(len(result)):
    print(result[i], end=" ") 