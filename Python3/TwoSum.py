# Two Sum
# Prompt:
#   Given an array of integers nums and an integer target, return indices of the two 
#   numbers such that they add up to target. You may assume that each input would have 
#   exactly one solution, and you may not use the same element twice. You can return the 
#   answer in any order.
#
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
#   -10^9 <= target <= 10^9
#   Only one valid answer exists.
#
# Example:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Output: Because nums[0] + nums[1] == 9, we return [0, 1].


from typing import Counter, List

def main():
    nums = [0, 4, 3, 0]
    target = 0

    print(twoSum(nums, target))

def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    A solution that is less than O(n^2) by utilizing a dictionary to map out the
    needed values
    '''
    differences = {}
    nums_size = len(nums)
    for x in range(nums_size):
        if nums[x] in differences:
            return [differences[nums[x]], x]
        differences[target - nums[x]] = x



# def twoSum(nums: List[int], target: int) -> List[int]:
#     '''
#     Brute force method
#     '''
#     nums_size = len(nums)
#     for x in range(nums_size):
#         for y in range(nums_size):
#             sum = nums[x] + nums[y]
#             if((sum == target) and x != y):
#                 return [x, y]      

main()
