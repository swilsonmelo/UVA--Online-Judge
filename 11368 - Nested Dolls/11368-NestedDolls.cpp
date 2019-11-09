#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct doll{
    int w , h;
    doll(int a = 0 , int b = 0){
        w = a , h = b;
    }
};
vector<doll> D , ans;
int m;

bool cmp(doll d1 , doll d2){
    if(d1.h == d2.h){
        return d1.w<d2.w;
    }
    return d1.h>d2.h;
}

void ini(){
    ans.clear();
    D.clear();
}

void readcase(){
    int w , h;
    scanf("%d" , &m);
    for(int i = 0; i < m; i++){
        scanf("%d%d" , &w , &h);
        D.push_back(doll(w , h));
    }
}

int Binary_search(int w){
    int l = 0 , r = ans.size()-1;
    while(l < r){
        int mid = (l+r)/2;
        if(ans[mid].w <= w) l = mid+1;
        else r = mid;
    }
    return l;
}

void computing(){
    sort(D.begin() , D.end() , cmp);
    
    for (int i = 0; i < D.size(); i++)
    {
        printf(" %d %d\n",D[i].w, D[i].h);
    }
    
    ans.push_back(D[0]);
    for(int i = 1; i < D.size(); i++){
        int tem = Binary_search(D[i].w);
        //cout << ans[tem].w << endl;
        if(ans[tem].w > D[i].w) ans[tem].w = D[i].w;
        else ans.push_back(D[i]);
    }
    printf("%d\n" , ans.size());
}

int main(){
    int t;
    scanf("%d" , &t);
    while(t--){
        ini();
        readcase();
        computing();
    }
    return 0;
}