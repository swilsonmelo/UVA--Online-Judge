#include<bits/stdc++.h>
#define mem(x) memset(x,0,sizeof x)

using namespace std;

int num[1050];

int solve(int n, int maxi){
	int sum = 0, cont = 0;
	for(int i = 0; i < n && sum != -1; i++){
		sum += num[i];
		if( sum == maxi) sum = 0, cont++;
		else if(sum > maxi) sum = -1;
	}
	return cont;
}

int main(){
	int n, maxi, res = -1, tmp;
	while( scanf("%d", &n) == 1 ){
		maxi = -1; res = -1; mem(num);
		for(int i =0; i < n; i++){
			scanf("%d", &num[i]); maxi = (num[i] > maxi) ? num[i] : maxi;
			
		}
		for(int i = 0; i < n-1 ; i++){
			res = max(solve(n,maxi),res);
			tmp = num[0];
			for( int j = 0; j < n-1; j++){
				num[j] = num[j+1];
			}	
			num[n-1] = tmp;
		}
		if( res > 2) printf("%d\n", res);
		else printf("%d\n", -1); 
	}
		
}
