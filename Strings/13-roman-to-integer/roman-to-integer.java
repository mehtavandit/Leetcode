class Solution {
    public int romanToInt(String s) {

        char[] c = s.toCharArray();
        int total = 0; 
        int last = 0;
        int current = 0;

        for (int i = s.length()-1; i>=0; i--){
            current = convertchar(c[i]);

            if (last>current){
                total = total-current;
                last = current;
                continue;
            }
            total = total + current;
            last = current;
        }
        return total;
        
    }

    public int convertchar(char c){
        int i=0;
        switch(c){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return i;
    }
}