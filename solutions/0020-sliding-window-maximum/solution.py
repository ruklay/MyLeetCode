from collections import deque

def sliding_window_maximum(nums, k):
    if not nums or k == 0:
        return []

    n = len(nums)
    if k == 1:
        return nums

    max_values = []
    dq = deque()

    for i in range(n):
        # Remove indices that are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements from the back of the deque that are smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element's index to the deque
        dq.append(i)

        # The front of the deque is the largest element for the current window
        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values