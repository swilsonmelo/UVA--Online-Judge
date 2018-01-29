
#include <bits/stdc++.h>
#define BOUND 1000005

using namespace std;

char str[BOUND];


int main(){
	int n,mini,maxj,x,y,cases;
	int same ;
	//freopen("in.txt","r",stdin);
	cases = 1;
	while( gets(str) ){
		printf("Case %d:\n",cases);
		scanf("%d",&n);
		for(int i = 1; i <= n; i++){
			same = 1;
			
			scanf("%d %d",&x,&y);
			mini = min(x,y);
			maxj = max(x,y);
			if(mini != maxj){
				
				
				char ant = str[mini];
				for(int j = mini+1; j <= maxj;j++){
					if(str[j]!=ant){
						same=0;
						printf("No\n");
						break;
					}
				}
				if(same) printf("Yes\n");
			}else printf("Yes\n");
		}
		getchar();
		//printf("%s hooly\n",str);	
		cases++;
	}
	
	
	return 0;
}
