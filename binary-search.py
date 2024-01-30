# we will compare naive and binary search to show binary search is faster.
# Naive search: iterate through the entire list and check if it equals the target.
# if the target is present in the list, return the index. 
# if not, then return -1

# Binary search: Look for the target in a sorted list using divide and conquer.

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
        
    if high < low:
        return -1
        
    # example list = [1, 3, 5, 10, 12]
    midpoint = (low + high) // 2 # we need to find the midpoint first
    
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint - 1)
    else:
        return binary_search(list, target, midpoint + 1, high)

if __name__ == '__main__':
    list = [1, 3, 5, 10, 12]
    target = 12
    print(naive_search(list, target))
    print(binary_search(list, target))
    