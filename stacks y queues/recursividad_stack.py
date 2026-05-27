def stack(arr):
    if arr == []:
        return
    else:
        arr.pop()
        stack(arr)


arr = [5,3,8,2,10]
stack(arr)