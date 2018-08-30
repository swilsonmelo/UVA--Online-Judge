#include <bits/stdc++.h>

using namespace std;


long long mat[25][25];

int n,n1;



long long recu(int x, int y){
	long long m1,m2;
	m1 = 0;
	m2 = 0;
	//printf("%d %d %d\n",x,y,n);
	if( mat[x][y] != -1){
		//printf("alvv");
		return mat[x][y];
	}else if( x >= y ){
		
		
		if( x == n ) m1 = 0;
		else{
			for(int k = x+1; k<= n; k++){
				m1 = max(m1, recu(k,1)+recu(k,y) );
			}
		}
		
		
		if( y == 0 ) m2 = 0;
		else{
			for(int k = 1; k < y; k++){
				m2 = max(m2, recu(x,k)+recu(n,k) );
			}
		}
		//printf("%d %d\n",m1,m2);
		mat[x][y] = m1 + m2;
		return mat[x][y];
	
	}else{
		
		//printf("puff\n");
		for(int k = x; k<y; k++){
			mat[x][y] = max(mat[x][y], recu(x,k) + recu(k+1,y) );	
		}
		//printf("aquí %d\n",mat[x][y]);
		return mat[x][y];
	}
}

int main(){
	while(scanf("%d %d",&n,&n1) == 2){
		
		memset(mat,-1,sizeof mat);
		//printf("%d",mat[10][10]);
		mat[n][1] = n1;
		//printf("%d  hollaa\n",mat[n][1]);
		printf("%lld\n",recu(1,n));
	
	}
	
	return 0;
}
