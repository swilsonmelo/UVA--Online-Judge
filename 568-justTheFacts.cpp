#include <bits/stdc++.h>
#define limit 10010

int salida[limit];
void precalc(int n){
	salida[0] = 1;
	long long m = 1;
	for(int i = 1; i <= n; i++){
		m = m * i;
		while(m % 10 == 0) m /= 10;
        m = m % 100000;
		salida[i] = m%10;
	}
	
	
	
	
}


int main(){
	precalc(10000);
	int n;
	//reopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	while(scanf("%d",&n) == 1 ){
		printf("%5d -> %d\n",n,salida[n]);
	}
	
	
	return 0;
}
