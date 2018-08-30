#include <bits/stdc++.h>

using namespace std;

int n;  
  
int main()  
{  
    while(~scanf("%d",&n)) {  
    	printf("%d\n",n/2); 
        if(n==1){	
			puts("");	        	
        }   
        else if(n%2==1){  
            while(n>3)  
            {  
                printf("2 ");  
                n-=2;  
            }  
            printf("3\n");  
        }  
        else{  
			printf("2"); 
            n-=2;  
            while(n>=2)  
            {  
                printf(" 2");  
                n-=2;  
            }  
            printf("\n");  
        }  
    }  
    return 0;  
}  
