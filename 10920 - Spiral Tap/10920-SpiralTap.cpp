#include <bits/stdc++.h>

using namespace std;
long  long n, num;


void solve(long long num){
	long long lim, posx, posy, ra, diag = 0;
	for(long long i = 1; i*i <= num; i += 2  ){
		diag++;
		lim = i*i;
		ra = i;
		posy = posx = diag + (n / 2);
	}
	//printf("num %d lim %d  posx %d posy %d ra %d\n",num,lim,posx,posy,ra);
	if(lim == num){
		printf("Line = %lld, column = %lld.\n", posy, posx);
		return;
	}else{
		lim += 1;
		posy += 1;
		if(num <= lim + ra){
			posx -= num - (lim );
			//printf("num %d lim %d  posx %d posy %d ra %d\n",num,lim,posx,posy,ra);
			printf("Line = %lld, column = %lld.\n", posy ,posx);
			return;
		}
		posx -= ra;
		lim += ra;
		ra+= 1;
		if(num <= lim + ra){
			posy -= num - (lim);
			//printf("num %d lim %d  posx %d posy %d ra %d\n",num,lim,posx,posy,ra);
			printf("Line = %lld, column = %lld.\n", posy ,posx);
			return;
		}
		posy -= ra;
		lim += ra;
		if(num <= lim + ra){
			posx += num - (lim);
			//printf("num %d lim %d  posx %d posy %d ra %d\n",num,lim,posx,posy,ra);
			printf("Line = %lld, column = %lld.\n", posy ,posx);
			return;
		}
		posx += ra;
		lim += ra;
		if(num <= lim + ra){
			posy += num - (lim);
			//printf("num %d lim %d  posx %d posy %d ra %d\n",num,lim,posx,posy,ra);
			printf("Line = %lld, column = %lld.\n", posy ,posx);
			return;
		}
		
	}
	printf("%ld %ld kha\n",num, lim);

	//printf("%d %d\n",lim,pos);
	
	
}


int main(){
	//freopen("in.txt","r",stdin);
	//int num;
	scanf("%ld %ld",&n,&num);
	while(n != 0 && num != 0){
		//printf("%ld %ld\n",n,num);
		solve(num);
		scanf("%d %d",&n,&num);
		//puts("case");
	}
	
	
	return 0;
}
