#include <bits/stdc++.h>

using namespace std;

map<int,int> posi;
int vec[10005];

int main(){
	int cases = 1,n,querys,x;
	//freopen("10474.txt","r",stdin);

	scanf("%d %d",&n,&querys);
	while( n!= 0 && querys!=0 ){
		for(int i = 0; i < n; i++) {
			scanf("%d",&vec[i]);
			
		}
		sort(vec,vec+n);
		
		for(int i=0; i < n; i++){
			if(posi[vec[i]] == 0) posi[vec[i]] = i+1;
		}
		
		
		printf("CASE# %d:\n",cases);
		for(int i = 0; i < querys; i++){
			scanf("%d",&x);
			if( posi[x] == 0 ) printf( "%d not found\n",x );
			else printf("%d found at %d\n",x,posi[x]);
		}
		cases++;
		posi.clear();
		scanf("%d %d",&n,&querys);
		
	}	
		
	
	
	return 0;
}
