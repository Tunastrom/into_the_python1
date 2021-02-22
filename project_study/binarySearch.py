# 2021/02/22

def binarySearch(array, value, low, high):
        if low > high:
            return False
        mid = (low+high)//2
        if array[mid] > value:
            return binarySearch(array, value, low, mid-1)
        elif array[mid] < value:
            return binarySearch(array, value, mid+1, high)
        else:
            return mid

NeedtoSearch_Num = range(0,20,2)
print_this=(binarySearch(NeedtoSearch_Num, 8, 0 , len(NeedtoSearch_Num)-1 ))
print(print_this) 


