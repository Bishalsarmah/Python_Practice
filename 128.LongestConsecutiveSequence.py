# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


def longestConsecutiveSequence(nums):
    nums.sort()
    n = len(nums)
    smallest = float("-inf")
    maxi = 0
    count = 0
    for i in range(0,n):
        if nums[i] - 1 == smallest:
            count += 1
            smallest = nums[i]
        elif nums[i] != smallest:
            count = 1
            smallest = nums[i]
        maxi = max(maxi,count)
    return maxi

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutiveSequence(nums))
