import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isIsomorphic(String s, String t) {

        int m = s.length();
        int n = t.length();
        if(n!=m){
            return false;
        }

        Map<Character, Character> dictionary = new HashMap<>();

        for(int i=0; i<n; i++)
        {
            char c = s.charAt(i);
            char value_to_check = t.charAt(i);
            if(dictionary.containsKey(c))
            {
                if (dictionary.get(c) != t.charAt(i)){
                    return false;
                }
                for (Map.Entry<Character, Character> entry : dictionary.entrySet()) 
                {
                    Character key = entry.getKey();
                    Character value = entry.getValue();
                    // System.out.println("Key: " + key + ", Value: " + value);
                    if(value.equals(value_to_check) && s.charAt(i) != key){
                        return false;
                    }
                }

            }
            else{
                for (Map.Entry<Character, Character> entry : dictionary.entrySet()) 
                {
                    Character key = entry.getKey();
                    Character value = entry.getValue();
                    // System.out.println("Key: " + key + ", Value: " + value);
                    if(value.equals(value_to_check) && s.charAt(i) != key){
                        return false;
                    }
                }
                dictionary.put(c, t.charAt(i));
            }

        }
        return true;

        
    }
}