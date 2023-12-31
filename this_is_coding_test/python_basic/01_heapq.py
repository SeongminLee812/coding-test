import heapq

def heapsort(iterable):
    h = []
    results = []
    # push all elements to heap
    for value in iterable:
        heapq.heappush(h, value)
    # append all elements in heap to list
    for _ in range(len(h)):
        results.append(heapq.heappop(h))
    return results

results = heapsort([1, 3, 6,7,8, 9, 9, 2, 21])
print(results)

def heapsort(iterable):
    h = []
    results = []
    # push all elements to heap
    for value in iterable:
        heapq.heappush(h, -value)
    # append all elements in heap to list
    for _ in range(len(h)):
        results.append(-heapq.heappop(h))
    return results


results = heapsort([1, 3, 6, 7, 8, 9, 9, 2, 21])
print(results)

