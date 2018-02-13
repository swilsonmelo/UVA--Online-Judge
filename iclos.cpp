#include <bits/stdc++.h>
#define loop(i,a,b) for(int i = a ; i < b; ++i)
#define FOR(i,b) for(int i = 0 ; i < b; ++i)
#define len(a) ((int)a.size())
#define LIM 100
#define pb(a) push_back(a)

// Detecta cantidad de ciclos de sub-arboles
// No usar si hay puntos de articulacion

using namespace std;

typedef vector<int> vi;
typedef vector<vi> Graph;

Graph G;
int parent[LIM];
vector<int> ant;

void printSet(int WHITE[],int GRAY[],int BLACK[],int n){
	FOR(i,n)cout << WHITE[i] << " ";
	puts("");
	FOR(i,n)cout << GRAY[i] << " ";
	puts("");
	FOR(i,n)cout << BLACK[i] << " ";
	puts("");
}

void moveSet(int node,int SRC[],int TGT[]){
	SRC[node] = 0 ;	TGT[node] = 1;
}

int dfs(int src,int WHITE[],int GRAY[],int BLACK[]){
	moveSet(src,WHITE,GRAY);//Voy a explorarlo
	FOR(i,len(G[src])){
		int u  = G[src][i];
		if(parent[u]!=-1)parent[u] = src;
		if(BLACK[u])continue; // vis[u] = true
		if(GRAY[u])return src; // Hay ciclo
		int  v = dfs(u,WHITE,GRAY,BLACK);
		if(v)return v;


	}
	moveSet(src,GRAY,BLACK);
	return 0;
}


int DectedCycleInDirectGraph(int WHITE[],int n){
	int GRAY[LIM];int BLACK[LIM],v;
	memset(GRAY,0,sizeof GRAY);
	memset(BLACK,0,sizeof BLACK);
	int CC = 0;
	FOR(i,n)if(WHITE[i]){
		parent[i] = -1;
		v = dfs(i,WHITE,GRAY,BLACK);
		if(v){
			//printSet(WHITE,GRAY,BLACK,n);
			//return v;
			CC++;
			ant.pb(v);
		}
	}
	return CC;
}

int main(){
	freopen("Cycle.txt","r",stdin);
    int n,e,u,v;G.clear();
    cin >> n >> e;
    int WHITE[LIM];
    G.assign(n,vi());
    ant.clear();
    memset(WHITE,0,sizeof WHITE);
    FOR(nodes,e){
		cin >> u >> v ;
		G[u].pb(v);
		WHITE[u] = 1;WHITE[v] = 1;
    }
    FOR(ni,n)parent[ni] = ni;
	int res = DectedCycleInDirectGraph(WHITE,n);
	cout <<"Hay "<<   res << " Ciclos" << endl;
		
	/*Pendiente
	stack <int> wayParent;
	wayParent.push(res);
	while(parent[res]!= -1){
		res  = parent[res];
		wayParent.push(res);
	}
	*/

	return 0;
}
