#include <bits/stdc++.h>

using namespace std;

//int vec[1000005];
map<int,int> func;

int solve(int n){
	//printf("%d %d\n",n,vec[n]);
	if(func[n] != 0){
		return func[n];
	}else{
		if(n%2 == 0){
			func[n/2] = solve(n/2);
			return func[n/2]+1;
		}else{
			func[3*n+1] = solve(3*n+1);
			return func[3*n+1]+1;
		}
	}
}


int main(){
	int x,y,mn,mx;
	int res = 0;
	//printf("%d",func[4]);
	//memset(vec,-1,sizeof vec);	
	
	//printf("%d",vec[100]);
	func[1] = 1;
	while(scanf("%d%d",&x,&y)==2){
		int res = 0;
		mx = max(x,y);
		mn = min(x,y);
		//printf("%d %d\n",x,y);
		for(int i = mn; i<=mx;i++){
			//printf("%d %d %d %d\n",mn,mx,i,res);
			//printf("%d %d\n",res,i);
			res = max(res,solve(i));
		}
		printf("%d %d %d\n",x,y,res);
	}
}

