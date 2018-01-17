#include <bits/stdc++.h>


#define BOUND 1000000
using namespace std;

int criba[BOUND] = {0};
vector<long> primes;


void seive(){
	
	//printf("%d %d\n",criba[2],criba[15]);
	criba[0] = criba[1] = 1;
	for(long long i = 2; i < BOUND; i++){
		if(!criba[i]){
			for(long long j = i*i; j < BOUND; j+= i){
				criba[j] = 1;
			}
		primes.push_back(i);
		}
	}
	criba[1] = 0; 
	//printf("%d %d\n",criba[2],criba[15]);
}


int is_prime(int x){
	int ra = sqrt(x);
	
	if( x < BOUND  ){
	
		return !criba[x];
	}
	else{
		for(int i = 0; i < primes.size(); i++){
			int prime = primes[i];
			if( prime > ra) return 1;
			else if( x % prime == 0) return 0;
		}
	}
	
	return 1;
}


int main(){
	seive();
	long n;
	long  r;
	//freopen("in.txt","r",stdin);
	scanf("%ld",&n);
	vector<int> fact;
	while(n!=0){
		r = n;
		fact.clear();
		
		if(n == 1){
			printf("1 = \n");
		}else if( r == -1 ){
			printf("-1 = -1 x \n");
		}else{
			printf("%d = ",r);
			if(n < 0){
				n *= -1;
				fact.push_back(-1);
			}
			if(!is_prime(n)){
				
				for(int i = 0; i < primes.size(); i++){
					
					int prime = primes[i];
					
					if(n%prime==0){
						
						fact.push_back(prime);
						n /= prime;
						//printf("%d x ",prime );
						while(n%prime == 0 && n != 1){
							
							
							fact.push_back(prime);
							n /= prime;
							
							//printf("%d x ",prime );
						}
					}
					if( n == 1 ) break;
					
				}
				
			}else {
				fact.push_back(n);
			}
			
			
			for(int i = 0; i < fact.size() -1 && fact.size() != 0; i++) printf("%d x ",fact[i]);
			if( fact.size() !=0 ) printf("%d",fact[fact.size()-1]);
			
			printf("\n");
			
			
		}
		scanf("%d",&n);
	}
	
	
	return 0;
}
