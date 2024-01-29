class Solution {
    public int longestConsecutive(int[] nums) {
       if(nums.length==0)
       {
           return 0;
       }
       int count=1;
       int max=1;
       Arrays.sort(nums);
       for(int i=1;i<nums.length;i++){
        //    if(nums[i]-nums[i-1]==0)continue; 0,0,1,2,3,4,5,6,7,8
           if(nums[i]-nums[i-1]==1)
           {
               count++;
           }
            if(count>max){
                max=count;
            }
            if(nums[i]-nums[i-1]>1)
                count=1;
            
       }
      return max;
    }
}