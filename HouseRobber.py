Leetcode problem https://leetcode.com/problems/house-robber/description/
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        prev2=0
        prev1=nums[0]
        # Iterate through the houses starting from the second house
        for i in range(1,len(nums)):
            #calculate max money for the current house
            current=max(prev1,nums[i]+prev2)
            prev2=prev1
            prev1=current
        return prev1                               
