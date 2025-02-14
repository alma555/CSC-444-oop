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
            temp_nums = nums.copy()
            current = temp_nums.pop(i)
            diff = target - current
            possible_result = self.twoSum(temp_nums, diff)
            if possible_result != None:
               possible_result.append(i)
            total = 0
            for j in possible_result:
                total += nums[j]
            if total == target:
                result = possible_result

        #postcondition: check that output is as specified
        if isinstance(result, list) != True:
            raise ValueError('result was not a list; result = ', result)
        return result

    def test(self):
        if self.threeSum([8,3,11,1],15) == [1,2,3]: #nums[1] + nums[2] + nums[3]
            print("Test 1 passed")
        else: print("Test 1 failed")
        if self.threeSum([0,0,8,1],8) == [0,1,2]: #nums[0] + nums[1] + nums[2]
            print("Test 2 passed")
        else: print("Test 2 failed")
        if self.threeSum([-6,-6,-6,-6,-6,-6],1) == []: #no possible answer
            print("Test 3 passed")
        else: print("Test 3 failed")

solve = ThreeSum()
solve.test()

#The time complexity of twoSum is O(n)
#The time complexity of threeSum is O(n^2); not very good!. i bet there's a way to make it faster with hashing, but that's not part of the assignment
#I am not a graduate student, I just wanted to answer the question
