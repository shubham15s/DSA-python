def getSecondLargest( arr):
        n = len(arr)
        
        large = float("-inf")
        second_large = float("-inf")
        
        for i in range(n):

            if arr[i] > large:
                second_large = large
                large = arr[i]
            elif arr[i] > second_large and arr[i] < large:
                second_large = arr[i]
        
        if second_large == float('-inf'):
            return -1
        
        return second_large


# arr = [12, 35, 1, 10, 34, 1]
arr = [10,20]

print("second largest element: ", getSecondLargest( arr))