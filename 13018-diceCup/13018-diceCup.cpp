

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
	int m,n,mx,mn;
	int cases = 0;
	//printf("%d %d\n",n,m);
	while (scanf("%d %d",&m,&n)==2){
		mx = max(m,n);
		mn = min(m,n);
		if(cases) puts("");
		cases = 1;
		
		for(int i =mn+1; i <=mx+1;i++){
			printf("%d\n",i);
		}
		
	}
	
	return 0;
}

