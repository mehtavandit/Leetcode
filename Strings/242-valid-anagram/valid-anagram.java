import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) 
    {
        Map<Character, Integer> dict1 = new HashMap<>();
        Map<Character, Integer> dict2 = new HashMap<>();
        char c;

        for(int i=0; i<s.length(); i++)
        {
            c = s.charAt(i);
            if(!dict1.containsKey(c))
            {
                dict1.put(c,1);
            }
            else
            {
                int value = dict1.get(c);
                value = value+1;
                dict1.put(c, value);
            }
        }

        for(int i=0; i<t.length(); i++)
        {
            c = t.charAt(i);
            if(!dict2.containsKey(c))
            {
                dict2.put(c,1);
            }
            else
            {
                int value = dict2.get(c);
                value = value+1;
                dict2.put(c, value);
            }
        }

        boolean areEqual = dict1.equals(dict2);

        return areEqual;
    }
}