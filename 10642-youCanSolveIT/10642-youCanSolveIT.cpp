#include <bits/stdc++.h>


using namespace std;


long long solve(int x,int y){
	long long r1,r2;
	r1 = abs(0-y);
	r2 = x + r1;
	r2 = (r2*(r2+1))/2;
	r2+=r1;
	return r2;
	
	
}

int main(){
	
	int cases;
	//freopen("in.txt","r",stdin);
	int x1,y1,x2,y2;
	scanf("%d",&cases);
	for(int i = 1; i<= cases; i++){
		scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
		long long dis1,dis2;
		dis1 = solve(x1,y1);
		dis2 = solve(x2,y2);
		long long r = dis2 - dis1;
		printf("Case %d: %lld\n",i,r);
		
	}
	
	
	return 0;
}
