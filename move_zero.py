# Given an array of nums, write a function that moves all zeros to the end of the array while maintaining the relative order of the non-zero elements.
class Solution:
    def move_zeroes(self, nums):
        for i in range(len(nums) -1):
            if nums[i] == 0:
                print(f"Original array is {nums}")
                print(f"0 occurs at {i}")
                temp = nums[i]
                n = (len(nums) - i)
                k = len(nums[i+1:])
                print(f"Array needs to be moved {nums[i+1:]}")
                print(f"Array to be overwritten {nums[i:i+k]}")
                nums[i:i+k] = nums[i+1:]
                nums[-1] = temp
                print(f"Rotated array is {nums}")

solution = Solution()
# solution.move_zeroes([0,1,0,3,12])
# solution.move_zeroes([0,0,0])
solution.move_zeroes([0,2,0,4,0,5])
# solution.move_zeroes([1,2,3,4,5])
# solution.move_zeroes([])
# solution.move_zeroes([0])
# solution.move_zeroes([0,1])
# solution.move_zeroes([1,0])
# solution.move_zeroes([0,0,1,0])
