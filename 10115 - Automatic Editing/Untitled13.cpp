#include<bits/stdc++.h>
using namespace std;
//10300 ecological
int main(){

    int T,n;
    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> n;
        int sum = 0,a,b,c;
        for(int i = 0; i < n; i++){
            cin >> a >> b >> c;
            sum += a*c;
        }
        cout << sum << endl;
    }
    return 0;
}
