#include <bits/stdc++.h>

using namespace std;


vector<int> arr;

void lotto(int n){
	for(int i = 0; i < n; i++){
		for(int j = i+1 ;j < n; j++){
			for(int k = j+1 ;k < n; k++){
				for(int l = k+1; l < n; l++){
					for(int m = l+1; m < n; m++){
						for(int o = m+1; o < n; o++){
							printf("%d %d %d %d %d %d\n",arr[i],arr[j],arr[k],arr[l],arr[m],arr[o]);
						}
					}
				}
			}
		}
	
	}
}



int main(){
	int n,x;
	freopen("in.txt","r",stdin);
	scanf("%d",&n);
	while(n!=0){
		arr.clear();
		for(int i = 0; i <n; i++){
			scanf("%d",&x);
			arr.push_back(x);
		}
		
		lotto(n);
		scanf("%d",&n);
		if(n) puts("");
	}
	
	
	
	
	return 0;
}
