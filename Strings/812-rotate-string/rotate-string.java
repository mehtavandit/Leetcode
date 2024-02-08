class Solution {
    public boolean rotateString(String s, String goal) {
        int n = goal.length();
        int m = s.length();

        if(n!=m){
            return false;
        }
        
        String doubles = s + s;
        if(doubles.contains(goal))
        {
            return true;
        }
        return false;
    }
}