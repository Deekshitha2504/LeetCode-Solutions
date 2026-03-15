int maxProfit(int* prices, int pricesSize) {
    int maxdif=0;
    int minp=prices[0];
    for(int i=0;i<pricesSize;i++){
        int curp=prices[i];
        if(curp<minp){
            minp=curp;
        }
        if((curp-minp)>maxdif){
            maxdif=curp-minp;
        }

    }
    return maxdif;
}