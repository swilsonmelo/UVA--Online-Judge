#include <bits/stdc++.h>
# define BOUND 10004
using namespace std;

vector<vector<int> > graph; 
int visit[BOUND];
int degree[BOUND];

int cycles;
stack<int> usados;
int nodos[BOUND];


int dfs(int src,int r){
	int u,v;
	nodos[src] = 0;
	for(int i = 0; i < graph[src].size(); i++){
		u = graph[src][i];
		nodos[u] = 0;
		//printf("%d %d %d \n",src,u,visit[u]);
		usados.push(src);
		if(visit[u] == 1) {
			if(r) cycles += 1;
			return 1;	
		}
		if(visit[src] == 2) return 0;
		
		visit[src] = 1;
		int v = dfs(u,r);
		
			while(!usados.empty()){
				visit[usados.top()] = 2;
				usados.pop();
			}
			
		
	}
	
	return 0;	
	
}

int main(){
	
	int cases,n,E,u,v;
	freopen("int.txt","r",stdin);
	scanf("%d",&cases);
	//printf("%d",cases);
	for(int x = 1; x <= cases; x++){
		cycles = 0;
		memset(degree,0,sizeof degree);
		memset(visit,0,sizeof visit);
		scanf("%d %d",&n,&E);
		graph.assign(n+1,vector<int>() );
		//printf("%d",graph.size());
		for(int i = 0; i < E; i++){
			scanf("%d %d",&u,&v);
			graph[u].push_back(v);
			nodos[v] = nodos[u] = 1; 
			degree[v] ++;
		}	
		/*
		puts("");
		
		for(int i = 1; i < graph.size(); i++){
			printf("%d ",i );
			for ( int j = 0; j < graph[i].size(); j++){
				printf("%d ", graph[i][j]);
			}
			printf("\n");
			
		}
		puts("");
		
		*/
		int r = 1;
		int temp;
		for(int i = 1; i <= n; i++){
			r = 1;
			if(degree[i] != 0 && nodos[i] == 1) dfs(i,r);
			
			 			
		}
		
		int mini = degree[1],cont = 0;
		if(degree[1] == 0) cont++;
		
		for(int i = 2; i <= n;i++){
			mini = min(degree[i],mini);
			if(degree[i] == 0) cont++;
			
		}
		
		//printf("%d %d %d \n",cycles,cont,mini);
		
		printf("Case %d: %d\n",x,cycles+cont);
		
		
								
	}
	
	
	
	return 0;
}
