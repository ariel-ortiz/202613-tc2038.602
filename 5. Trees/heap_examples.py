# type: ignore

from heapq import heappush, heappop # for min-heap
from heapq import heappush_max, heappop_max # for max-heap (new in Python 3.14)

def heap_sort(data):

    # Create the heap
    heap = []
    for elem in data:
        heappush(heap, elem)

    # Remove one element at a time from the heap
    result = []
    while heap:
        result.append(heappop(heap))

    return result

def heap_sort_reverse(data):

    # Create the heap
    heap = []
    for elem in data:
        heappush_max(heap, elem)

    # Remove one element at a time from the heap
    result = []
    while heap:
        result.append(heappop_max(heap))

    return result
    

if __name__ == '__main__':
    # heap = []
    # heappush(heap, 7)
    # print(heap)
    # heappush(heap, 4)
    # print(heap)
    # heappush(heap, 10)
    # print(heap)
    # heappush(heap, 2)
    # print(heap)    
    # heappush(heap, 3)
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    print(heap_sort([7, 5 ,8, 6, 10, 2, 4, 1]))
    print(heap_sort_reverse([7, 5 ,8, 6, 10, 2, 4, 1]))
