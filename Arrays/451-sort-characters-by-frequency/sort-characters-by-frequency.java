class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> dict = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        int n = s.length();

        for(int i=0; i<n; i++)
        {
            char c = s.charAt(i);
            if(!dict.containsKey(c))
            {
                dict.put(c,1);
            }
            else
            {
                int current_value = dict.get(c);
                int incremented_value = current_value+1;
                dict.put(c, incremented_value);
            }
        }

        dict.entrySet().stream().sorted(Map.Entry.<Character, Integer>comparingByValue().reversed()).forEach(record -> {
          Character key = record.getKey();
          int value = record.getValue();
          for(int i = 0; i < value; i++) {
              sb.append(key);
          }
      });
      return sb.toString();
    }
}