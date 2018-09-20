#include <bits/stdc++.h>

using namespace std;

vector<int> pila;

int main(){
	//freopen("in.txt","r",stdin);
	int n,u,v;
	scanf("%d",&n);
	while( n!= 0){
		
		int padres[n+1];
		int pesos[n+1];
		int deGree[n+1];
		for(int i = 0; i<= n+1; i++ ) {
			padres[i] = 0;
			deGree[i] = -1;
		}
		for(int i = 0; i < n; i++ ){
			scanf("%d",&u);
			scanf("%d %d",&pesos[u],&deGree[u]);
			for(int j = 0; j < deGree[u]; j++){
				scanf("%d",&v);
				padres[v] = u;
			}
		}
		pila.clear();
		for(int i = 1; i <= n; i++) {
			if(!deGree[i]) pila.push_back(i);
		}
		
		/*
		for(int i= 0; i < pila.size(); i++) printf("%d ", pila[i]);
		printf("\n");
		*/
		int costo = 0, sobra,padre;
		while(!pila.empty()){
			u = pila[pila.size()-1];
			pila.pop_back();
			padre = padres[u];
			deGree[padre] --;
			sobra = pesos[u] - 1;
			costo += abs(sobra);
			pesos[u] = 1;
			pesos[padre] += sobra;
			if( deGree[padre] == 0 ){
				pila.push_back(padre);
			}
			
		}
		printf("%d\n",costo);
		scanf("%d",&n);
	}
	return 0;
}
