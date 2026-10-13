class Solution {
    public int maxProfit(int[] prices) {
        int maxprof=0;
        int curlow=prices[0];
        for(int x:prices){
            if (x<curlow){
                curlow=x;
            }
            int diff= x-curlow;
            if (diff>maxprof){
                maxprof=diff;
            }
        }
        return maxprof;
    }
}