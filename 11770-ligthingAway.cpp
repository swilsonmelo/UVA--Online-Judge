
/*
REVISAR PORQUE NO FUNCIONA!!!!!!!!!
*/

#include <bits/stdc++.h>
# define BOUND 10004
using namespace std;

vector<vector<int> > graph; 
int visit[BOUND];
int degree[BOUND];

int cycles;
int nodos[BOUND];
vector<pair<int,int> > topo;

int dfs(int src,int r){
	int u,v;
	visit[src] = 2;
	for(int i = 0; i < graph[src].size(); i++){
		u = graph[src][i];
		if(visit[u] == 1) {
			cycles += 1;
			visit[u] = 2;
			visit[src] = 2;
			continue;	
		}
		if(visit[u] == 2) continue;
		
		visit[src] = 1;
		int v = dfs(u,r);
		visit[src] = 2;
		visit[u] = 2;
		
	}
	
	return 0;	
	
}

int main(){
	
	int cases,n,E,u,v;
	freopen("int.txt","r",stdin);
	scanf("%d",&cases);
	for(int x = 1; x <= cases; x++){
		cycles = 0;
		memset(degree,0,sizeof degree);
		memset(visit,0,sizeof visit);
		topo.clear();
		scanf("%d %d",&n,&E);
		graph.assign(n+1,vector<int>() );
		for(int i = 0; i < E; i++){
			scanf("%d %d",&u,&v);
			graph[u].push_back(v);
			degree[v] ++;
			
		}	
		pair<int,int> pa;
		for(int i = 1; i <= n; i++) {
			pa.first = degree[i];
			pa.second = i;
			topo.push_back(pa);	
		}
		
		sort(topo.begin(),topo.end());
		int r = 1;
		int temp;
		for(int i = topo.size()-1; i >= 0; i--){
			pa = topo[i];
			if( visit[pa.second] != 2) {
				//for(int j = 0; j < topo.size(); j++) printf("%d %d  topoo %d  ",degree[topo[j].second],topo[j].second,visit[topo[j].second]);
				//puts("");
				cycles ++;
				//printf("%d aqui \n",pa.second);
				temp = cycles;
				dfs(pa.second,r);
				if(temp < cycles) cycles = temp ;
	
				
			}
				 			
		}
		memset(visit,0,sizeof visit);
		int cycles1 = cycles;
		cycles = 0;
		r = 1;
		temp;
		for(int i = 0; i < topo.size(); i++){
			pa = topo[i];
			if( visit[pa.second] != 2) {
				//for(int j = 0; j < topo.size(); j++) printf("%d %d  topoo %d  ",degree[topo[j].second],topo[j].second,visit[topo[j].second]);
				//puts("");
				cycles ++;
				//printf("%d aqui \n",pa.second);
				temp = cycles;
				dfs(pa.second,r);
				if(temp < cycles) cycles = temp ;
	
				
			}
				 			
		}
		
		printf("Case %d: %d\n",x,min(cycles1,cycles));						
	}
	
	
	
	return 0;
}
