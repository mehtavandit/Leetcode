class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List <Integer> result = new ArrayList<>();
        long n = nums.length;
        long compare = n/3;
        Arrays.sort(nums);
        int counter = 1;
        for(int i=0; i<n-1;i++)
        {
            if(nums[i] == nums[i+1])
            {
                counter++;
                if(!result.contains(nums[i]) && counter>compare)
                {
                    result.add(nums[i]);
                }
            }
            else{
                if(counter>compare)
                {
                    if(!result.contains(nums[i]))
                    {
                        result.add(nums[i]);
                    }
                }
                counter = 1;
            }
        }
        int last_element = nums[(int)n-1];
        int last_counter = 1;
        if(!result.contains(last_element)  && last_counter>compare)
        {
            result.add(last_element);
        }
        return result;

    }
}