#include <bits/stdc++.h>


using namespace std;
int x,y;


void findNumber(int n){

    int ini,pos,z;
	ini = 1;
    for(int i = 1; i < n+1; i += 2){
    	
    	z = i*i;
        if(z>n){
            ini = i;
            break;
    	}
    }
    //printf("%d %d %d %d \n",ini,x,y,n);
    ini -= 2;
    pos = ini;
    x = ini/2; 
    y = ini/2; 
    ini = ini*ini;
    //printf("%d %d %d %d \n",ini,x,y,n);
    if (n == ini)return;
    ini += 1;
    x += 1;
    //printf("%d %d %d %d \n",ini,x,y,n);
    if(n == ini)return;
    //printf("%d %d %d %d %d \n",ini,x,y,n,pos);
    if(ini+pos >= n){
    	y -= (n-ini);
    	return;
    }
        
    ini = ini+pos;
    y -= pos;
    pos += 1;
    //printf("%d %d %d %d \n",ini,x,y,n);
    if(ini+pos >= n){
    	x -= n-ini;
    	return;
    }
    x -= pos;
    ini = ini+pos;
    //printf("%d %d %d %d \n",ini,x,y,n);
    if(ini+pos >= n){
    	y += (n-ini);
    	return;
    }
        
    ini = ini+pos;
    y+= pos;
    pos -= 1;
    //printf("%d %d %d %d \n",ini,x,y,n);
    if(ini+pos >= n){
    	x += (n-ini);
    	return;
    }
	//printf("hhh\n");   	
}

int getNum(int x, int y) {
    int w = max(abs(x), abs(y));
    int z = w*2+1;
    int v = z*z, tx = w, ty = w;
    if(ty == y)
        return v - abs(tx-x);
    v -= z, tx = -w, ty = w-1;
    if(tx == x)
        return v - abs(ty-y);
    v -= z-1, ty = -w, tx = -w+1;
    if(ty == y)
        return v - abs(tx-x);
    v -= z-1, tx = w, ty = -w+1;
    if(tx == x)
        return v - abs(ty-y);
    return 0;
}


int main() {
	
	//freopen("in.txt","r",stdin);
    int n, i, j;
    while(scanf("%d", &n) == 1) {
        findNumber(n);
        int a = x, b = y;
        //printf("%d %d \n",x,y);
        for(i = 1; i >= -1; i--){
            for(j = -1; j <= 1; j++){
                printf("%d;", getNum(a+j, b+i));
            }
        	printf("\n");
        }
    }
    return 0;
}
