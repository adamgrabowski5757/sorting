## Common Sorting Algorithms
## By Adam Grabowski
## Includes: Bubble, Merge, and Quick Sorts

"""
Bubble Sort Implementation:

Input: Array

Output: Int, Number of comparisons done through sorting. 

Sorts input array in-place. 

"""
def bubble_sort(a):
    num_compares = 0
    for x in range(len(a)-1,0,-1):
        for i in range(x):
            num_compares = num_compares + 1
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return num_compares



"""
Merge Sort Implementation:

Input: Array

Output: Int, Number of comparisons done through sorting. 

Sorts input array in-place. merge_sort calls merge_sort_recursive 
so that merge_sort can be called with only array as input

"""
def merge_sort(a):
    count = 0
    return merge_sort_recursive(a, count)

def merge_sort_recursive(a, count):
    count = count +1
    if len(a)>1:
        ## split input array 
        middle = len(a)//2
        left = a[:middle]
        right = a[middle:]

        ## Recursively sort two halves of input array
        merge_sort_recursive(left, count)
        merge_sort_recursive(right, count)
        
        ## initialize indices for arrays, used in merging
        leftcount=0
        rightcount=0
        i=0
        
        ## merge arrays and sort
        while leftcount < len(left) and rightcount < len(right):
            count = count + 3
            if left[leftcount] < right[rightcount]:
                a[i]=left[leftcount]
                leftcount=leftcount+1
            else:
                a[i]=right[rightcount]
                rightcount=rightcount+1
            i=i+1
        count = count + 2
        ## residual sorting on left array
        while leftcount < len(left):
            count = count + 1
            a[i]=left[leftcount]
            leftcount=leftcount+1
            i=i+1
        count = count + 1
        ## residual sorting on right array
        while rightcount < len(right):
            count = count + 1
            a[i]=right[rightcount]
            rightcount=rightcount+1
            i=i+1 
        count = count + 1
    return count


"""
Quick Sort Implementation:

Input: Array

Output: Int, Number of comparisons done through sorting. 

Sorts input array in-place. quick_sort calls quick_sort_recursive 
so that quick_sort can be called with only array as input. quick_sort_recursive additionally
uses quick_sort_partition to sort. 

"""
def quick_sort(a):
    count = []
    low_idx = 0
    high_idx = len(a)-1
    
    quick_sort_recursive(a, low_idx, high_idx, count)
    
    return len(count)


def quicksort_partition(a, low_idx, high_idx, count):
    pivot = a[high_idx]
    i = low_idx - 1
    for j in range(low_idx, high_idx):
        count.append(1)
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[high_idx] = a[high_idx], a[i+1]
    return i+1

def quick_sort_recursive(a, low_idx, high_idx, count):
    count.append(1)
    if low_idx < high_idx:
        ## find pivot
        p = quicksort_partition(a, low_idx, high_idx, count)
        ## Recurse on sub arrays
        quick_sort_recursive(a, low_idx, p-1, count)
        quick_sort_recursive(a, p+1, high_idx, count)
    return 
    