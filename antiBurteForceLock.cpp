#include <bits/stdc++.h>

using namespace std;

vector< pair<int,pair<int,int> > > graph;
int padres[505];
int n;


int buscar(int x){
	if (padres[x] != x){
		padres[x] = buscar(padres[x]);
	}
	return padres[x];
}


void unin( int x, int y ){
	int xraiz = buscar(x); 
	int yraiz = buscar(y);
	if(xraiz != yraiz) padres[yraiz] = xraiz;
}

int kruskal(){
	int cost = 0;
	for(int i=0 ; i< graph.size(); i++){
		int x = graph[i].second.first;
		int y = graph[i].second.second;
		if( buscar(x) != buscar(y) ){
			cost += graph[i].first;
			unin(x,y);
		}
	}
	return cost;
}

int main(){
	
	vector <char *> nodos;
	int cases;
	freopen("in.txt","r",stdin);
	scanf("%d",&cases);
	char linea[5000];
	pair<int,pair<int,int> >edge;
	int dis = 0;
	int min1,min2;
	while(cases--){
		graph.clear();
		nodos.clear();
		scanf("%d",&n);
		for(int i = 0; i < n; i++) padres[i] = i;
		
		gets(linea);
		char * spliter;
		spliter = strtok(linea," ");
		for(int i = 0; i < n; i++){
			nodos.push_back(spliter);
			spliter = strtok(NULL," ");
		}
		
		for(int i = 0; i < nodos.size()-1; i++){
			for(int j = i+1; j < nodos.size(); j++){
				dis = 0;
				
				for(int k = 0; k < 4 ; k++){
					min1 = min2 = 100;
					min1 = min(abs(nodos[i][k]-nodos[j][k]),abs(nodos[j][k]-nodos[i][k]));
					min2 = min(abs(nodos[i][k]-nodos[j][k]+10),abs(nodos[j][k]-nodos[i][k]+10));
					dis += min(min1,min2);
				}
				edge.first = dis;
				edge.second.first = i;
				edge.second.second = j;
				graph.push_back(edge);
			}
		}
		sort(graph.begin(),graph.end());
		
		/*
		for(int i = 0; i < graph.size(); i++) printf("%d %d %d\n",graph[i].first,graph[i].second.first,graph[i].second.second);
		
		
		puts("");
		
		for(int i = 0; i < graph.size(); i++) printf("%d %d %d\n",graph[i].first,graph[i].second.first,graph[i].second.second);
		
		
		for(int i = 0; i <n; i++){
			printf("%s\n",nodos[i]);
		}
		*/
		int z = kruskal();
		int r = 100;
		for(int i = 0; i < nodos.size(); i++ ) {
			dis = 0;
			for(int k = 0; k < 4 ; k++){
					min1 = min2 = 100;
					min1 = min(abs(nodos[i][k] - '0'),abs('0'- nodos[i][k]));
					min2 = min(abs(nodos[i][k] - '0'+10),abs('0' - nodos[i][k]+10));
					dis += min(min1,min2);
			}
			r = min(r,dis);	
		}
		printf("%d\n",r+z);
	}
	
	
	
	
	return 0;
}
