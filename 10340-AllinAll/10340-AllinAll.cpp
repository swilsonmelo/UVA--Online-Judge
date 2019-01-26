#include <bits/stdc++.h>

using namespace std;


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    string s1, s2;
    int n, pos;
    while( cin >> s1 >> s2 ){
        n = s1.size();
        pos = 0;
        for(int i = 0; i < s2.size() && pos < n; i++){
            if(s1[pos] == s2[i]) pos++;
        }
        if(pos == n) cout << "Yes" << endl;
        else cout << "No" << endl;

    }


    return 0;
}
