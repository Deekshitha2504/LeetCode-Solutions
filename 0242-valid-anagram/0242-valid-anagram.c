bool isAnagram(char* s, char* t) {
  if(strlen(s)!=strlen(t)){
    return false;
  }

  int count[26]={0};
  for(int i=0;s[i]!='\0';i++){
    count[s[i]-'a']++;
    count[t[i]-'a']--;}
  for(int j=0;j<26;j++){
    if(count[j]!=0){
        return false;}
    }
    return true;  
  }  
