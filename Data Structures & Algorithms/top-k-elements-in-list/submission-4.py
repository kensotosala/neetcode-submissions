class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Add the numbers to a dict
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] = dict_nums.get(num, 0) + 1
            else:
                dict_nums[num] = 1

        # 2. Sort a dict
        sorted_dict = dict(sorted(dict_nums.items(), key=lambda x: x[1], reverse=True))

        # 3. Return K elements
        result = []
        keys = list(sorted_dict.keys())
        for i in range(k):
            result.append(keys[i])

        return sorted(result)
        