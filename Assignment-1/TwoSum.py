from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers on a list which sum to a target number

        Args:
            nums (List[int]): the input list
            target (int): the target number

        Return: 
            list: two numbers which sum to target
        """

        #precondition: check that all inputs are as specified
        if nums != list:
            raise ValueError('target must be a list of integers')
        for i in list:
            if i != int:
                raise ValueError('target must be a list of integers')
        if target != int:
            raise ValueError('target must be an integer')
        
        hash = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                result = [hash[diff], i]
            hash[nums[i]] = i
        
        #postcondition: check that output is as specified
        if result != list:
            raise ValueError('output was not a list; output = ', output)

        return result
