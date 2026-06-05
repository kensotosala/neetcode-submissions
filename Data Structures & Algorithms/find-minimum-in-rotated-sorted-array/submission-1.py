class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_index = 0
        right_index = len(nums)
        min_num = nums[0]

        mid_index = 0

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if mid_index >= len(nums) or mid_index < 0:
                return min_num
            mid_number = nums[mid_index]

            if mid_number < min_num:
                min_num = mid_number

            if mid_number > min_num:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        return min_num
