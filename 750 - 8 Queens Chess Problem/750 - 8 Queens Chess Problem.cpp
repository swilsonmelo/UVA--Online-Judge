#include <bits/stdc++.h>

using namespace std;


int row[8],x,y,solution;


int place(int r, int c){
	for(int prev = 0; prev < c; prev++){
		if( row[prev] == r || ( abs(row[prev] - r) ) == abs(prev - c) ) return 0;
	}	
	return 1;
	
}

void backtrack(int c){
	if( c == 8 && row[y] == x){
		printf("%2d      %d", solution++, row[0] + 1);
		for(int i = 1; i < 8; i++) printf(" %d", row[i] + 1);
		printf("\n");
	}
	for(int r = 0; r < 8; r++){
		if(place(r,c)){
			row[c] = r;
			backtrack(c+1);
		}
	}
	
	
}


int main(){
	int tc;
	//freopen("in.txt","r",stdin);
	scanf("%d",&tc);
	for( int c = 0; c < tc; c++){
		scanf("%d %d",&x,&y);
		x -=1; y -= 1;
		solution = 1;
		memset(row,0,sizeof row);
		printf("SOLN       COLUMN\n");
		printf(" #      1 2 3 4 5 6 7 8\n\n");
		backtrack(0);
		if( c != tc-1 ) printf("\n");
			
	}
	return 0;
}
