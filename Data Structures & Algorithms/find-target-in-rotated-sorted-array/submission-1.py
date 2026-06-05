class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Si encontramos el objetivo
            if nums[mid] == target:
                return mid

            # Determinar si la mitad izquierda está ordenada
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Si la mitad derecha está ordenada
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        # Si no se encuentra el objetivo
        return -1
