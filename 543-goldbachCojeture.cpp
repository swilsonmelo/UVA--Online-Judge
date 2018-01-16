#include <bits/stdc++.h>

using namespace std;

#define BOUND 1000000

int criba[BOUND] = {0};
vector<long> primes;
void seive(){
	criba[0] = criba[1] = 1;
	for(long long i =  3; i < BOUND; i+= 2){
		if(!criba[i]){
			for(long long j = i*i; j < BOUND; j+= i){
				criba[j] = 1;
			}			
		primes.push_back(i);
		}
			
	}
}


int is_prime(int x){
	int z = sqrt(x);
	int prime;
	for(int i = 0; i < primes.size(); i++){
		prime = primes[i];
		if( prime > z) return 1;
		else if( x % prime == 0) return 0;	
		
	}
	return 0;
	
}


int main(){

	seive();
	int n;
	int encontrados = 0;
	//freopen("in.txt","r",stdin);
	scanf("%d",&n);
	while(n!=0){
		int p1;
		int p2;
		encontrados = 0;
		for(int i = 0; i < primes.size() && !encontrados; i++){
			p1 = primes[i];
			p2 = n - p1;
			//printf("%d %d hgjh\n",criba[9],criba[15]);
			if(p2 < BOUND) encontrados = !criba[p2];
			else encontrados = is_prime(p2);
			//printf("%d alvvv\n",!criba[p2]);
			
		}
		printf("%d = %d + %d\n",n,p1,p2);
		scanf("%d",&n);
	}
	
	
	return 0;
}
