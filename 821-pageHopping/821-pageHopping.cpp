#include <bits/stdc++.h>
#define infi 100000

using namespace std;

int floydWar[102][102];

int main(){
	freopen("in.txt","r",stdin);
	int a,b,cases= 1;
	scanf("%d",&a);
	scanf("%d",&b);
	while ( a!= 0 and b != 0){
		
		for(int i = 0; i <= 100;  i++){
			for(int j = 0; j <= 100; j++){
				floydWar[i][j] = infi;
			}
		}
		
		while ( a!= 0 and b != 0){
			floydWar[a][b] = 1;	
			scanf("%d",&a);
			scanf("%d",&b);			
		}
		
		//algoritmo de floydWarshall
		for(int k = 0; k <= 100; k++){
			for(int i = 0; i <= 100; i++){
				for(int j = 0; j <=100; j++ ){
					floydWar[i][j] = min(floydWar[i][j],floydWar[i][k] + floydWar[k][j]);
				}
			}
		}
		
		int suma = 0;
		int coneccted = 0;
		for(int i = 0; i<= 100; i++){
			for(int j = 0; j <= 100; j++){
				if( i != j && floydWar[i][j] != infi){
					suma += floydWar[i][j];
					coneccted ++;
				} 
			}
			
		}
		printf("Case %d: average length between pages = %.3lf clicks\n",cases,(1.0*suma/coneccted));
		
		scanf("%d",&a);
		scanf("%d",&b);
		cases ++;
		
	}
	
	
}
