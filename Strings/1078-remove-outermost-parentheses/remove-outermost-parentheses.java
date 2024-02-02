class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();

        int counter = 0;

        for(int i=0; i<n; i++)
        {
            if(s.charAt(i) == '(')
            {
                counter++;
                if(counter>1)
                {
                    sb.append("(");
                }
            }
            else
            {
                counter--;
                if(counter>=1)
                {
                    sb.append(")");
                }
            }
        }
        return sb.toString();
    }
}