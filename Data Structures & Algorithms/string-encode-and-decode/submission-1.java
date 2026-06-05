class Solution {

    // Delimiter to separate length and actual string
    private static final char DELIMITER = ':';

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String str : strs) {
            int length = str.length();
            encoded.append(length).append(DELIMITER).append(str);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            // Find the delimiter to extract length
            int delimiterIndex = str.indexOf(DELIMITER, i);
            if (delimiterIndex == -1) break;
            
            int length = Integer.parseInt(str.substring(i, delimiterIndex));
            i = delimiterIndex + 1 + length;
            decoded.add(str.substring(delimiterIndex + 1, i));
        }
        return decoded;
    }
}
