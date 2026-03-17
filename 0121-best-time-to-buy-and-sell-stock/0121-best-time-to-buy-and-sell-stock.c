int maxProfit(int* prices, int pricesSize) {
    int maxdif=0;
    int min=prices[0];
    for(int i=1; i<pricesSize; i++){
        int cur=prices[i];
        if(min>cur){
            min=cur;
        }
        int curdif=cur-min;
        if(curdif>maxdif){
            maxdif=curdif;
        }
    }
    return maxdif;
}