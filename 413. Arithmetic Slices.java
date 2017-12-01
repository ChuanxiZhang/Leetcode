public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int count = 0 , gap = 0;
        for (int i = 0; i < A.length - 2 ; i++){
            gap= A[i+1]-A[i];
            for (int j = i + 2; j <A.length ; j++){
                int k = 0 ;
                for (k = i + 1; k <= j ; k++){
                    if (A[k]-A[k-1] != gap){
                        break;
                    }
                }
                if (k > j){
                    count++;
                }
            }
        }
        return count;
    }
}
