def product_except_self(nums):
    length = len(nums)
    
    # Initialize the left and right product arrays
    left_products = [1] * length
    right_products = [1] * length
    
    # Fill the left_products array
    for i in range(1, length):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    # Fill the right_products array
    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    # Build the result array by multiplying left and right products
    result = [1] * length
    for i in range(length):
        result[i] = left_products[i] * right_products[i]
    
    return result