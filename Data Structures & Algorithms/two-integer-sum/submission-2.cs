public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        List<int[]> result = new List<int[]>();
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++) 
            {
                if (nums[i] + nums[j] == target)
                {
                    int[] pair = new int[] { i, j };

                    result.Add(pair);
                }
            }
        }

        if (result.Count > 0)
        {
            return result[0];
        }
        
        return new int[0]; 
    }
}
