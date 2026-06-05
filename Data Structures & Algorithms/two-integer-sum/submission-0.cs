public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        List<int[]> result = new List<int[]>();

        HashSet<int> used = new HashSet<int>();

        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++) 
            {
                if (nums[i] + nums[j] == target)
                {
                    int[] pair = new int[] { i, j };

                    result.Add(pair);

                    used.Add(nums[i]);
                    used.Add(nums[j]);
                }
            }
        }

        if (result.Count > 0)
        {
            return result[0];
        }
        else
        {
            return new int[0]; 
        }
    }
}
