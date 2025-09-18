# Given an array of nums, write a function that moves all zeros to the end of the array while maintaining the relative order of the non-zero elements.
class Solution:
    def move_zeroes(self, nums):
        for i in range(len(nums) -1):
            if nums[i] == 0:
                temp = nums[i]
                n = (len(nums) - i)
                k = len(nums[i+1:])
                print(f'0 occurs at {i}, \n\
                        array after 0 is {nums[i+1:]}, \n\
                        number of array items to be moved will be {len(nums[i+1:])}, \n\
                        array to be overwritten {nums[i:i+k]} \n\
                    ')
                # print(nums[i:])

solution = Solution()
solution.move_zeroes([0,1,0,3,12])
