from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers on a list which sum to a target number

        Args:
            nums (List[int]): the input list
            target (int): the target number

        Return: 
            list: indices of two numbers which sum to target
        """
        
        #precondition: check that all inputs are as specified
        if isinstance(nums,list) != True:
            raise ValueError('input must be a list of integers')
        for i in nums:
            if isinstance(i,int) != True:
                raise ValueError('input must be a list of integers')
        if isinstance(target,int) != True:
            raise ValueError('target must be an integer')
        
        hash = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                result = [hash[diff], i]
            hash[nums[i]] = i
        
        #postcondition: check that output is as specified
        if isinstance(result, list) != True:
            raise ValueError('result was not a list; result = ', result)

        return result
