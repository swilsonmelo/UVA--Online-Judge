#include <bits/stdc++.h>
using namespace std;

//typedef vector<int> vi;


int color[205];
vector<int> graph[205];

int bfs(int start){
	queue<int> q;
	q.push(start);
	color[start] = 1;
	while (!q.empty()){
		int u = q.front();
		q.pop();
		for (int i = 0; i < graph[u].size(); i++){
			int v = graph[u][i];
			if (color[v] == -1){
				color[v] = 1 - color[u];
				q.push(v);
			}
			else if (color[v] == color[u]) return 0;
		}
		
	}
	
	
	
	
	return 1;
	
	
}



int main(){
	//freopen("in.txt","r",stdin);
	int nodes, edges, u, v;
	scanf("%d",&nodes);
	while (nodes){
		scanf("%d",&edges);
		for (int i = 0; i < nodes; i++) {
			graph[i].clear();
			color[i] = -1;	
		}
		for (int i = 0; i < edges; i++){
			scanf("%d",&u);
			scanf("%d",&v);
			graph[u].push_back(v);
			graph[v].push_back(u);
		}
		
		if (bfs(0)) printf("BICOLORABLE.\n");
		else printf("NOT BICOLORABLE.\n");
		
		/*
		for (int i = 0; i < nodes; i++){
			printf("%d :",i);
			for (int j = 0; j < graph[i].size(); j++) printf("%d ",graph[i][j]);
			puts("");
		}
		
		puts("");
		*/
		scanf("%d",&nodes);
		
	}
	
	
	
	
	return 0;
}
