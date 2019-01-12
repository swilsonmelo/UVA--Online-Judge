#include <bits/stdc++.h>

using namespace std;

char str[11111];

int main() {

	
	while (scanf("%s", str) == 1) {
		int sz = strlen(str);
		int res = 0;;
        int cont = 0;
        for(int pos = 0; pos<sz; pos++){
        	if(str[pos] == '0'){
        		if(cont == 0 || cont == 1){
        			res+=1;
        			cont=0;
        		}
        		else cont -= 1;        			
        	}
        	else if(str[pos] == '1'){
        		if(cont == 0) cont = 2;
        		else cont+= 1;
        	}else{
        		
        		if(cont == 0 || cont == 1){
        			res+=1;
        			cont=0;
        		}
        		else cont -= 1;    			
        	
        	}
        
        }
            
        if(cont == 0) printf("%d\n",res);
        else printf("0\n");
	
	}
	return 0;
}
