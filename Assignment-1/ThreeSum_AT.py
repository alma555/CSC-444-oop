from typing import List
from TwoSum_AT import Solution

class ThreeSum(Solution):
    def threeSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds three numbers on a list which sum to a target number

        Args:
            nums (List[int]): the input list
            target (int): the target number

        Return:
            list: indices of three numbers which sum to target
        """

        #precondition: check that all inputs are as specified
        if isinstance(nums,list) != True:
            raise ValueError('input must be a list of integers')
        for i in nums:
            if isinstance(i,int) != True:
                raise ValueError('input must be a list of integers')
        if isinstance(target,int) != True:
            raise ValueError('target must be an integer')

        result = []
        for i in range(len(nums)):
            temp_nums = nums
            current = temp_nums.pop(i)
            diff = target - current
            possible_result = self.twoSum(temp_nums, diff).append(diff)
            total = 0
            print(possible_result)
            for j in possible_result:
                total += nums[j]
            if total == target:
                result = others
                break

        #postcondition: check that output is as specified
        if isinstance(result, list) != True:
            raise ValueError('result was not a list; result = ', result)
        return result

    def test(self):
        if self.threeSum([8,3,11,1],15): #nums[1] + nums[2] + nums[3]
            print("Test 1 passed")

solve = ThreeSum()
solve.test()
#print(test.threeSum((8,3,11,1),15)) #nums[1] + nums[2] + nums[3]
#print(test.threeSum((0,0,8,1),8)) #nums[0] + nums[1] + nums[2]
#print(test.threeSum(-6,-6,-6,-6),1) #no numbers add up to 1
