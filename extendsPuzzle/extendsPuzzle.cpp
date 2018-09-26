#include <bits/stdc++.h>
# define MAX 100002
using namespace std;

int puzzle[MAX];
int pos[MAX];

int main(){
	freopen("in.txt","r",stdin);
	freopen("ou.txt","w",stdout);
	int n,m,total,x,pasos;
	scanf("%d %d",&n,&m);
	while( n*m != 0 ){
		pasos = 0;
		total = n*m;
		for( int i = 1; i <= total; i++){
			scanf("%d",&x);
			puzzle[i]  = x;
			pos[x] = i;
		}
		/*for( int i = 1; i <= total; i++) printf("%d ",puzzle[i]);
		puts("");
		for( int i = 1; i <= total; i++) printf("%d ",pos[i]);
		puts("");*/
		int temp1,temp2,pos2;
		for(int i = 1;i <= total; i++){
			if(puzzle[i] != i){
				pos2 = pos[i];
				pos[i] = i;
				temp1 = puzzle[i];
				puzzle[i] = i;
				pos[temp1] = pos2;
				puzzle[pos2] = temp1;
				pasos += 1;
				
			}
		}
		if( pasos%2 == 0 )printf("Y\n",pasos);
		else printf("N\n",pasos);
		//printf("%d\n",pasos);
		scanf("%d %d",&n,&m);
	}
	
	
	return 0;
}
