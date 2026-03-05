import java.util.Scanner;
class Solution {
    public int removeDuplicates(int[] nums) {
        Scanner s=new Scanner(System.in);
        int i=1,j;
        for( j=1;j< nums.length;j++){
            if(nums[j] != nums[i-1]){
                nums[i]=nums[j];
                i=i+1;
            }
        }
        return i;
        
    }
}
