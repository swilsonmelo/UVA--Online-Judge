#include <bits/stdc++.h>


using namespace std;


long long dp[305][305];


void coinChange(){
	dp[0][0] = 1;
	for(int i = 1; i <= 300; i++){
		for(int j = i; j<=300; j++){
			for(int k = 1; k<= j; k++){
				dp[j][k] += dp[j-i][k-1];
			}						
		}
	}
		
	
	
}

int main(){
	
	freopen("in.txt","r",stdin);
	coinChange();
	char str[1000];
	int n;
	int num[3];
	while(gets(str)){
		n = 0;
		char *pch;
		pch = strtok(str," ");
		while(pch != NULL){
			num[n] = atoi(pch);
			n++;
			pch = strtok(NULL," ");
		}
		/*
		for(int i = 0; i < n; i++) printf("%d\n",num[i]);
		puts("");
		*/
		int l1,l2;
		//printf("%d\n",n);
		if(n == 1){
			l1 = 0;
			l2 = num[0];
		}else if(n==2){
			l1 = 0;
			l2 = num[1];
		}else{
			l1 = num[1];
			l2 = num[2];
		}
		if(l2 > num[0]) l2 = num[0];
		long long res = 0;
		//printf("%d %d %d allvv\n",l1,l2,num[0] );
		for(int i = l1; i <= l2; i++) res += dp[num[0]][i];
		printf("%lld\n",res);
		
		
	}

	return 0;
}
