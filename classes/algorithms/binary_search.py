def bs(arr, head, tail, x):
    if head >= tail:
        return head

    mid = (head + tail) // 2
    if x <= arr[mid]:
        tail = mid
    else:
        head = mid + 1

    return bs(arr, head, tail, x)


def bs2(arr, head, tail, x):
    if head >= tail:
        return head

    mid = (head + tail) // 2
    if x <= arr[mid]:
        return bs2(arr, head, mid, x)

    return bs2(arr, mid+1, tail, x)
