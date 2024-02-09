class Solution {
    public int maxDepth(String s) {
        int current_depth  = 0;
        int local_depth = 0;

        for(int i=0; i<s.length(); i++)
        {
            if(s.charAt(i) == '(')
            {
                local_depth = local_depth+1;
                if(local_depth>current_depth){
                    current_depth = local_depth;
                }
            }
            if(s.charAt(i) == ')'){
                local_depth = local_depth -1;
            }
        }
        return current_depth;
    }
}