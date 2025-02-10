class Solution:
    def twoSum(self, nums, target):

        hashtable = {}
    
        for i in range(len(nums)): #cycle through every item in the list. we need to keep track of the position, so we're actually checking every *position* for an item
            if (target - nums[i]) in hashtable: #for every item in the list, check whether it matches with an existing item in the hash table
                return (i,hashtable[target - nums[i]]) #if it does match with an existing item, return the position of both items
            else: 
                hashtable[nums[i]]=i #otherwise, store the position of the item in the hashtable. if it matches with an item later in the list, we can return the position
       

    def test(self):
        if self.twoSum((0,1,3),4) == (2,1): 
            print ("Test 1 passed")
        if self.twoSum((0,0,10,0,4),14) == (4,2):
            print("Test 2 passed")
        if self.twoSum((0,0),0) == (1,0):
            print("Test 3 passed")

solve = Solution()
solve.test()
