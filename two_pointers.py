def two_pointers(arr:list[int], target:int):
    left:int = 0
    right:int = len(arr) -1

    while left < right:
        sum:int = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left+=1
        else:
            right-=1
    return []

result = two_pointers([10,20,40,60,100], 80)
if len(result) == 0:
    print("No result found!!!")
else:
    # print there by comma separated
    print(result[0],',',result[1])

  