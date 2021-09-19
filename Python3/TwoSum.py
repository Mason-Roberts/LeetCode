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


# First attempts at a version that is less than O(n^2) runtime
# def twoSum(nums: List[int], target: int) -> List[int]:
#     possible_nums = []
#     index = 0
#     for num in nums:
#         if(num <= target):
#             possible_nums.append((num, index))
#         index += 1
#     possible_nums.sort()
#     return possible_nums


def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    Brute force method
    '''
    nums_size = len(nums)
    for x in range(nums_size):
        for y in range(nums_size):
            sum = nums[x] + nums[y]
            if((sum == target) and x != y):
                return [x, y]      

main()
