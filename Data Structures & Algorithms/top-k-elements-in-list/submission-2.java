class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Create a hash map to store the frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        
        // Count the frequency of each element in the array
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        // Create a priority queue to store the elements based on their frequency
        // The priority queue will be sorted based on the frequency in descending order
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> frequencyMap.get(b) - frequencyMap.get(a));
        
        // Add all the elements to the priority queue
        pq.addAll(frequencyMap.keySet());
        
        // Create an array to store the k most frequent elements
        int[] result = new int[k];
        
        // Extract the top k elements from the priority queue
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll();
        }
        
        return result;
    }
}