#include <bits/stdc++.h>

using namespace std;

int inDegree[101];
vector< int > graph[101];
int main(){
	int V,E,u,v;
	scanf("%d %d",&V,&E);
	while( V != 0 && E != 0){
		for(int i = 0; i < V; i++){
			graph[i].clear();
			inDegree[i] = 0;
		}
		for(int i = 0; i < E; i++){
			scanf("%d %d",&u,&v);
			
			inDegree[v] ++;
		}
		
		
		scanf("%d %d",&V,&E);	
	}
	
	return 0;
}
