#include <bits/stdc++.h>

using namespace std;

char c[205][205];
int vis[205][205];
int n;
int x[6] = {-1,-1,0,0,1,1 };
int y[6] = {-1,0,-1,1,0,1 };
int z;

void black(int p, int q){
	if(p == n-1){
		z = 1;
		return;
	} 
	vis[p][q] = 1;
	int a,b;
	for(int i = 0; i < 6; i++ ){
		a = p +  x[i];
		b = q  + y[i];
		if( a > 0 && b > 0 && a < n && b < n && c[a][b] == 'b' && !vis[a][b]) black(a,b);
	}
	
}

int main(){
	int cases = 1;
	freopen("in.txt","r",stdin);
	scanf("%d",&n);
	while( n!= 0){
		printf("%d ",cases);
		memset(vis,0,sizeof vis);
		for(int i = 0; i < n; i++)scanf("%s",c[i]);;
		z = 0;
		for(int i = 0; i < n; i++){
			if(z) break;
			if(c[0][i] == 'b'&& !vis[0][i]) {
				//printf("%d\n",i);
				black(0,i);
			}
		} 
		/*
		puts(" ");
		for(int i = 0; i < n ; i++){
			for(int j = 0; j < n; j++){
				printf("%d ",vis[i][j]);
			}
			printf("\n");
		}
		*/
		if(z) printf("B\n");
		else printf("W\n");
		scanf("%d",&n);
		cases++;	
	}
	
	return 0;
}
