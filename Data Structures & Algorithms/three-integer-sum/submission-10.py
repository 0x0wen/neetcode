class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        left, mid, right = 0, 1, len(nums) - 1
        while nums[left] <= 0 and mid < right:
            if nums[left] + nums[mid] + nums[right] == 0:
                res.append([nums[left], nums[mid], nums[right]])
                mid += 1
            elif (nums[left] + nums[mid]) * -1 > nums[right]:
                mid += 1
            elif (nums[left] + nums[mid]) * -1 < nums[right]:
                right -= 1
            elif (nums[mid] + nums[right]) * -1 < nums[left]:
                left += 1
                mid = left + 1 or mid != left + 1
            if mid == right:
                left += 1
                mid = left + 1
                right = len(nums) - 1
        res = [list(x) for x in dict.fromkeys(map(tuple, res))]
        return res