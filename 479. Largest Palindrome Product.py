class Solution {
    public int largestPalindrome(int n) {
        if(n == 1){
            return 9;
        }
        int upperbound = (int)Math.pow(10, n) - 1;
        int lowerbound = (int)upperbound / 10;
        for (int v = upperbound - 1; v > lowerbound; v--){
            long val = Long.valueOf(v + new StringBuilder().append(v).reverse().toString());
            for (long i = upperbound; i * i >= val; i--)
                if (val % i == 0)
                    return (int) (val % 1337);
        }
    return 0;
    }
}

  
