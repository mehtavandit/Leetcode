class Solution {
     public static String helper(String num, int i) {
        if(i<=0)
            return "";
        if ((num.charAt(i - 1) - '0') % 2 == 1)
            return num;
        return helper(num.substring(0,i-1),i-1);
    }
    public static String largestOddNumber(String num) {
        return helper(num,  num.length());
    }
}