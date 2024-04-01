"""
The code you provided implements the SLX (Select Larger or Equal) algorithm, which performs a binary search to find the smallest element in a sorted list A that is greater than or equal to x.
using the method of binary search
"""
def SLX(A, i, j, x):
    if i == j:
        if A[i] >= x:
            return A[i]
        else:
            return -1
    else:
        mid = (i+j) // 2
        if A[mid] < x:
            return SLX(A, mid+1, j, x)
        elif A [mid] >= x:
            return SLX(A, i, mid, x)

A = [1,2,4,5,6]
x = 3
print(SLX(A,0,5,x))
