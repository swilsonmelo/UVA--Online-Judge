#include <bits/stdc++.h>

using namespace std;

static const int MINUS_INF = -(25 * 25);




int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int cases;
	string s;
	scanf("%d",&cases);
	cin.ignore();
	getline(cin,s);
	for(int ca = 0; ca < cases; ca++){
		vector< vector<int> > M;
		int r = 0;
		int col;
		while( getline(cin, s) && s != "" ){
			col = s.size();
			M.push_back( vector<int>() );
			for(int c = 0; c < s.size(); c++){
				if( s[c] == '0' ){
					M[r].push_back(MINUS_INF);	
				}else{
					M[r].push_back(1);	
				} 
				
				if( r > 0 ) M[r][c] += M[r-1][c];
				if( c > 0 )	M[r][c] += M[r][c-1];
				if( r > 0 && c > 0) M[r][c] -= M[r-1][c-1];
				
			}
			r++;
			
			
		}
		/*
		//printf("%d %d\n",r,col);
		for(int i = 0; i < r; i++){
			for(int j = 0; j < col; j++) printf("%d ",M[i][j]);
			puts("");
			
		}*/
		//printf("kha %d\n",r);
		int maxSubRect = 0;
		
		for(int i = 0; i < r; i++){
			for(int j = 0; j < r; j++){
				for(int si = i; si < r; si++){
					for(int sj = j; sj < r; sj++){
						
						int subRect = M[si][sj];
						
						if( i > 0 ){
							subRect -= M[i-1][sj];	
						} 
						if( j > 0 ){
							subRect -= M[si][j-1];	
						} 
						if( i > 0 && j > 0 ){
							subRect += M[i-1][j-1];	
						} 
						
						maxSubRect = max(maxSubRect, subRect);
						
					}
				}
				
			}
		}
		printf("%d\n",maxSubRect);
		if(ca != cases-1) puts("");
		
	}
	
	return 0;
}
