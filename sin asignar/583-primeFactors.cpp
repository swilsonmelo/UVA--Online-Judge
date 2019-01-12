#include <bits/stdc++.h>
#define BOUND 1000000
using namespace std;

int seive[BOUND];
 
vector<int> primes;


void criba(){
	memset(seive,0,sizeof seive);
	
	seive[0] = seive[1] = 1;
	
	for(long long i = 0; i < BOUND; i++){
		if(!seive[i]){
			for(long long j = i*i; j < BOUND; j += i){
				seive[j] = 1;
			}
			primes.push_back(i);
		}
		
	}
	seive[1] = 1;
	//printf("%d %d\n",seive[2],seive[15]);
	
	
}


int main(){
	criba();
	int n ;
	//freopen("in.txt","r",stdin);
	scanf("%d",&n);
	while(n!=0){
		printf("%d =",n);
		if( n < 0 ){
			printf(" -1 x");
			n*=-1;
		}
		if(n != 1){
			int x;
			int i = 0;
			int prime;
			while(n != 1 ){
				x = sqrt(n);
				prime = primes[i];
				int isprime = 1;
				if(prime > x ){
					printf(" %d",n);
					break;
				}
				if(n % prime == 0){
					printf(" %d",prime);
					n /= prime;
					isprime = 0;
				}
				if(n == 1  ) break;
				else if(!isprime) printf(" x");
				
				if(n%prime !=0 ) i++;
			}
		}
		printf("\n");
		scanf("%d",&n);		
	}
	
		
	
	
	return 0;
}
