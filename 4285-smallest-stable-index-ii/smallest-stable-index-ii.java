class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n=nums.length;
        int small[]=new int[nums.length];
        small[n-1]=nums[n-1];
        for(int i=n-2;i>=0;i--)
        {
            small[i]=Math.min(small[i+1],nums[i]);
        }
        int large=nums[0];
        for(int i=0;i<n;i++)
        {
            large=Math.max(large,nums[i]);
            if(large-small[i]<=k)
            return i;
        }
        return -1;
    }
}