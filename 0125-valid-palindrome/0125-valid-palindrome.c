bool isPalindrome(char* s) {
   int left =0;
   int right= strlen(s)-1;
   while(left<=right){
    if(!isalnum(s[left])){
        left++;
    }
    else if(!isalnum(s[right])){
        right--;
    }
    else{
    if(tolower(s[right])!=tolower(s[left])){
        return false;
    }
    right--;
    left++;
    }

   }
   return true;
}