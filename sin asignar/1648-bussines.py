from sys import stdin
"""#include <cstdio>

int main(){
	
    int n, m;

  	while(scanf("%d%d", &n, &m) == 2){
  		
      	int ans = 1000000000;
        while(m--){
        	int u, d;
            scanf("%d%d", &u, &d);
            if((n*d) % (u+d) == 0) { if(u+d < ans) ans = u+d; }
            else{
				int x = (n*d) / (u+d) + 1;
                int t = x*(u+d)-n*d;
                if(t < ans) ans = t;
             }
         }
         printf("%d\n", ans);
     }
 
     return 0;
 }
"""
def main():
    en  = [int(x) for x in stdin.readline().strip().split()]
    while en:
        n = en[0]
        m = en[1]
        ans = 100000000
        for i in range(m):
            u,d = [int(x) for x in stdin.readline().strip().split()]
            x = d*n/(u+d)+1
            print(int(x),round(x))
            ans = min(ans,u*x-d*(n-x))
        print(ans)
        en  = [int(x) for x in stdin.readline().strip().split()]
main()
