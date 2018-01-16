#include <bits/stdc++.h>

using namespace std;


vector<pair<int, int> > twimP(100001);
vector<bool> prime(20000000, true);

int posi = 1;
int primeAnt = 0;

int main(){
	for( long long i = 3; posi <= 100000; i += 2){
		
		if( prime[i] ){
			for( long long j = i*i; j < 18409202; j += i){
				prime[j] = false;
			}
			
			if( i == primeAnt + 2  ){
				twimP[posi].first = primeAnt;
				twimP[posi].second = i;
				posi ++;
			}
			primeAnt = i;
		}
		
		
		
	}
	
	int n;
	while (scanf("%d",&n) == 1){
		printf("(%d, %d)\n",twimP[n].first,twimP[n].second);
		
	}
	
	
	return 0;
}
