#include<bits/stdc++.h>

using namespace std;


int main() {
	//freopen("in.txt","r",stdin);
	int n;
    while (cin >> n) {
        priority_queue <int> q;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            q.push(x);
        }
        bool can = true;
        while (!q.empty()) {
            int next = q.top(); q.pop();
            if (q.size() < next) {
                can = false;
                break;
            }
            vector <int> edges;
            for (int i = 0; i < next; i++) {
                int xi = q.top(); q.pop();
                edges.push_back(xi - 1);
            }
            for (int i = 0; i < next; i++) {
                if (edges[i] == 0) continue;
                q.push(edges[i]);
            }
        }
        if (can) cout << "1" << endl;
        else cout << "0" << endl;
    }
    return 0;
}
