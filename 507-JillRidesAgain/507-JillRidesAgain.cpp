#include <bits/stdc++.h>

using namespace std;



int resL = -1, resR = -1, currL = 0, currR = 0;
long maxSum = 0, currSum = 0;
vector<int> ArrayNums;

void kadane(){
	//printf(" kha   %d \n",maxSum);
	for(int i = 0; i < ArrayNums.size(); i++ ){
		if( currSum < 0 ){
			currL = i, currR = i + 1, currSum = ArrayNums[i];
		}else{
			currR = i + 1;
			currSum += ArrayNums[i];
		}
		
		if( (maxSum < currSum ) || ( maxSum == currSum && currR - currL > resR - resL ) ){
			resL = currL, resR = currR, maxSum = currSum;
		}
	}
	
}

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int cases, nums, val;
	scanf("%d",&cases);
	for(int i = 1; i <= cases; i++){
		scanf("%d",&nums);
		ArrayNums.clear();
		resL = -1, resR = -1;
		maxSum = 0, currSum = 0, currL = 0, currR = 0;

		for(int j = 0; j < nums - 1; j++){
			scanf("%d",&val);

			ArrayNums.push_back(val);
		}
		//printf("%d\n",nums);
		//for(int k = 0; k < ArrayNums.size(); k++) printf("%d ",ArrayNums[k]);
		//puts("");
		kadane();
		
		//printf("%d\n",maxSum);
		if( maxSum > 0) printf("The nicest part of route %d is between stops %d and %d\n",i,resL+1,resR+1);
		else printf("Route %d has no nice parts\n",i);
	
	}	
	
	
	return 0;
}

