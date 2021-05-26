import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxheapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


# result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
result = maxheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
