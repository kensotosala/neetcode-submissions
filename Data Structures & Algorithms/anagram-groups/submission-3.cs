public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        if (strs == null || strs.Length == 0) return new List<List<string>>();
        
        Dictionary<string, List<string>> map = new Dictionary<string, List<string>>();
        foreach (string s in strs) {
            char[] charArray = s.ToCharArray();
            Array.Sort(charArray);
            string sorted = new string(charArray);
            
            if (!map.ContainsKey(sorted)) {
                map[sorted] = new List<string>();
            }
            map[sorted].Add(s);
        }
        
        return new List<List<string>>(map.Values);
    }
}