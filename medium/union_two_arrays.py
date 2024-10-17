def findUnion(arr1,arr2,n,m):
        i, j = 0, 0  # Initialize two pointers
        result = []  # To store the union

        # Traverse both arrays using two pointers
        while i < n and j < m:
            # If arr1[i] is smaller, and it's not a duplicate
            if arr1[i] < arr2[j]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            # If arr2[j] is smaller, and it's not a duplicate
            elif arr1[i] > arr2[j]:
                if len(result) == 0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1
            # If both are equal, add any one of them and move both pointers
            else:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1

        # Add remaining elements from arr1
        while i < n:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        # Add remaining elements from arr2
        while j < m:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
n, m = len(arr1), len(arr2)

result = findUnion(arr1, arr2, n, m)
print(result) 