/*
MISMO CÖDIGO SOLO QUE MÄS ORDEN, REVISAR PORQUE EL OTRO NO PASA
*/
#include <bits/stdc++.h>


using namespace std;

#define MM 100005

int n, m, caseno, cases;
vector <int> adj[MM];
bool visited[MM];

vector <int> topo;

void dfs (int u ) {
    if( visited[u] ) return;
    visited[u] = true;
    for( int i = 0; i < adj[u].size(); i++ ) dfs( adj[u][i] );
    topo.push_back(u);
}

int main() {
	freopen("int.txt","r",stdin);
    scanf("%d", &cases);
    for(int x = 1; x <= cases; x++){
        int i;
        scanf("%d %d", &n, &m);
        for( i = 0; i < n; i++ ) adj[i].clear();
        for( i = 0; i < m; i++ ) {
            int u, v;
            scanf("%d %d", &u, &v);
            u--, v--;
            adj[u].push_back(v);
        }
        
        topo.clear();
        for( i = 0; i < n; i++ ) visited[i] = false;
        for( i = 0; i < n; i++ ) dfs(i);

        for( i = 0; i < n; i++ ) visited[i] = false;
        int cnt = 0;
        
        for(int i = topo.size()-1; i >= 0 ; i--){
        	
        	if(!visited[ topo[i] ]){
        		dfs(topo[i]);
        		cnt++;
        	}
        }

        printf("Case %d: %d\n",x, cnt);
    
    
    }
    return 0;
}
