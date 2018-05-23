#include <bits/stdc++.h>
using namespace std ;

//typedef pair<int,int> ii;

int n,m,fi,fj,ri,rj;
int pos[110][110];
int dis[110][110];

int xi[8] = {-2,-2,-1,1,-1,1,2,2};
int xj[8] = {-1,1,-2,-2,2,2,-1,1};

int rx[8] = {-1 ,-1,-1,0,0,1,1,1};
int ry[8] = {-1,0,1,-1,1,-1,0,1};

void llenar(int x, int y){
	for(int i = 0; i < 8; i++){
		int x1 = x + xi[i], y1 = y +xj[i];
		//printf("%d %d hollaa\n",x1,y1);
		if(x1 >= 0 && x1 < n && y1 >= 0 && y1 < m ){
			if(pos[x1][y1] != -2 && pos[x1][y1] != 2) pos[x1][y1]= -1;
		}
	}
}

int bfs(int x, int y){
	memset(dis,-1,sizeof dis);
	queue< pair<int,int> > q;
	dis[x][y] = 0;
	q.push( pair<int,int>(x,y) ) ;
	while(!q.empty()){
		
		pair<int,int> u = q.front();
		q.pop();
		if(u.first == fi && u.second == fj) return dis[u.first][u.second];
		for(int i = 0; i < 8; i++){
			int x1 = u.first + rx[i], y1 = u.second +ry[i];
		
			if(x1 >= 0 && x1 < n && y1 >= 0 && y1 < m ){
				 if( (pos[x1][y1]!=-1 && pos[x1][y1]!=-2)&& dis[x1][y1]==-1){
                    dis[x1][y1] = dis[u.first][u.second] + 1;
                    q.push(pair<int,int>(x1,y1));
				
				}		
			
			}
		}
		
	}
	return -1;
}

int main(){
	int cases;
	char letter[110];
	freopen("11352-crazyKing.txt","r",stdin);
	scanf("%d",&cases);
	
	while(cases--){
		scanf("%d %d",&n,&m);
		memset(pos , 0 , sizeof pos);
		for(int i = 0; i < n; i++){
			scanf("%s%*c",&letter);
			for(int j = 0; j < m; j++){
				
				if(letter[j] == 'Z'){
					llenar(i,j);
					pos[i][j] = -2;
				
				}if(letter[j]== 'B'){
					fi = i;
                    fj = j;
                    pos[i][j]=2;
					
				}if(letter[j] == 'A'){
					ri = i;
					rj = j;
				}
				//printf("%d %d %c\n",i,j,letter[j]);
			}
		}
		
		int res = bfs(ri,rj);
		if(res == -1){
			printf("King Peter, you can't go now!\n");
		}else{
			printf("Minimal possible length of a trip is %d\n",res);
		}
		/*
		for(int i = 0; i < n; i++){
			for(int j = 0 ; j < m ; j++){
				printf("%d ",pos[i][j]);
			}
			puts("");
		}
		*/
	}
	
	
	
}
