class Solution{
    public void moveZeroes(int[] nums){
        int nz=0, n=nums.length;
        for(int i=0; i<n; i++){
            if(nums[i]!=0){
                nums[nz]=nums[i];
                nz++;
            }
        } 
        for(int i=nz; i<n; i++){
            nums[i]=0;
        }
    }
}