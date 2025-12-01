from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count the frequency of each element in the nums list
    frequency = Counter(nums)
    
    # Use a min-heap to keep track of the top k elements
    min_heap = []
    
    for num, freq in frequency.items():
        # Push the current frequency and number onto the heap
        heapq.heappush(min_heap, (freq, num))
        
        # If the heap exceeds size k, remove the smallest frequency element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract the numbers from the heap and return them
    return [num for freq, num in min_heap]