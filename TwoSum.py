'''
https://leetcode.com/problems/two-sum/description/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_map = {}
        for idx, num in enumerate(nums):
            temp_map[num]=idx
        for idx, num in enumerate(nums):
            temp_data = target - num
            if temp_data in temp_map and temp_map[temp_data] !=idx:
                return [idx,temp_map[temp_data]]
