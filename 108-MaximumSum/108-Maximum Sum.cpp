#include <bits/stdc++.h>

using namespace std;

int mat[101][101];

int main(){
	int n;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	while( scanf("%d",&n) == 1){	
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++ ){
				scanf("%d",&mat[i][j]);
				/*
				La casilla mat[i][j] tendra la suma de la submatriz (0,0)-(i,j)
				*/
				if( i > 0) mat[i][j] += mat[i-1][j];
				if( j > 0) mat[i][j] += mat[i][j-1];
				if( i > 0 && j > 0) mat[i][j] -= mat[i-1][j-1];
			}
		}
				
		int maxSubRect = -127 * 100 * 100;		
		for(int i = 0; i < n; i++){			
			for(int j = 0; j < n; j++){				
				for(int k = i; k < n; k++){					
					for(int l = j; l < n; l++){						
						int subRect	= mat[k][l];						
						if( i > 0 ){
							subRect -= mat[i - 1][l];			
						} 
						if( j > 0 ) {
							subRect -= mat[k][j - 1];	
						}
						if( i > 0 && j > 0 ) {
							subRect += mat[i - 1][j - 1];	
						}
						maxSubRect = max(maxSubRect, subRect);	
					}
				}
			}
		}
	
		printf("%d\n", maxSubRect);
		/*
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++) printf("%d ",mat[i][j]);
			printf("\n");
		}*/
		
	}
	return 0;
}

