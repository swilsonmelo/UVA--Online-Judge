#include <bits/stdc++.h>

using namespace std;


int main(){
	int cases,x,y,res;
	scanf("%d",&cases);
	
	for(int i = 0; i < cases; i++){
		res = 0;
		scanf("%d %d",&x,&y);
		for(int j = x; j <= y; j++){
			if(j%2 != 0) res += j;
		}
		printf("Case %d: %d\n",i+1,res);
	}
	
	return 0;
}
