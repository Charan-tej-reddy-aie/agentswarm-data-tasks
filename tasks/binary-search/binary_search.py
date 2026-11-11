def binary_search(values, target):
    if not isinstance(values, list):
        raise TypeError()
    lo,hi=0,len(values)-1
    while lo<hi:
        mid=(lo+hi)//2
        if values[mid]==target:
            return mid
        if values[mid]<target:
            lo=mid+1
        else:
            hi=mid-1
    return None
