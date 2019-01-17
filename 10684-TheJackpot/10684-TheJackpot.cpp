#include <bits/stdc++.h>
#define MaxLen 10001


using namespace std;

int vec[MaxLen];

int kadane(int n){
	int currSum = 0, maxSum = 0;
	for(int i = 0; i < n; i++){
		if(currSum < 0){
			currSum = vec[i];
		}else{
			currSum += vec[i];
		}
		
		if(maxSum < currSum){
			maxSum = currSum;
		}
	}
	return maxSum;	
}


int main(){
	
	//freopen("in.txt","r",stdin);	
	//freopen("out.txt","w",stdout);
	
	int n;
	scanf("%d",&n);
	while( n != 0 ){
		
		for(int i = 0; i < n; i++){
			scanf("%d",&vec[i]);
		}
		
		int res = kadane(n);
		if(res > 0) printf("The maximum winning streak is %d.\n",res);
		else printf("Losing streak.\n",res);
		
		
		scanf("%d",&n);
	
	}
	return 0;
}
