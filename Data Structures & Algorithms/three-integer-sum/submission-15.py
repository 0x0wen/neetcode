class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer =set()
        for i in range(len(nums)):
          
            print(i)
            print(nums[i])
            res = 0- nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                evaluate = nums[right]+nums[left]
                if  evaluate == res:
                    answer.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                elif evaluate>res:
                    right -=1
                else:
                    left+=1
        return [list(r) for r in answer]