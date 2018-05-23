#include <bits/stdc++.h>
using namespace std;

const int dr[4] = {0, 0, +1, -1};
const int dc[4] = {+1, -1, 0, 0};
const int dir[4] = {'R', 'L', 'D', 'U'};
const int INF = 0x3f3f3f3f;
const int FOUND = -1;
vector<char> path;
int A[15][15], Er, Ec;

int H() {
    int h = 0;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (A[r][c] == 0) continue;
            int expect_r = (A[r][c] - 1) / 4;
            int expect_c = (A[r][c] - 1) % 4;
            //printf("A[i][j]%d  expect_r %d expect_C %d\n",A[r][c],expect_r,expect_c);
            h += abs(expect_r - r) + abs(expect_c - c);
        }
    }
    //printf("en H h %d\n",h);
    return h;
}

int dfs(int g, int pdir, int bound) {
    int h = H();
    //printf("%d\n",h);
    int f = g + h;
    if (f > bound) return f;
    if (h == 0) return FOUND;

    int mn = INF;
    for (int i = 0; i < 4; i++) {
        if (i == (pdir ^ 1)) continue;

        int nr = Er + dr[i];
        int nc = Ec + dc[i];
        if (nr < 0 || nr >= 4) continue;
        if (nc < 0 || nc >= 4) continue;

        path.push_back(dir[i]);
        swap(A[nr][nc], A[Er][Ec]);
        swap(nr, Er); swap(nc, Ec);
        int t = dfs(g + 1, i, bound);
        if (t == FOUND) return FOUND;
        if (t < mn) mn = t;
        swap(nr, Er); swap(nc, Ec);
        swap(A[nr][nc], A[Er][Ec]);
        path.pop_back();
    }

    return mn;
}

bool IDAstar() {
    int bound = H();
    for (;;) {
    	//printf("Bound %d\n", bound);
        int t = dfs(0, -1, bound);
        //printf("%d %d %d\n",Er,Ec,t);
        if (t == FOUND) return true;
        if (t == INF) return false;
        // ????? bound >= 50,?????? >= 50,??
        if (t >= 50) return false;
        bound = t;
    }
    return false;
}

bool solvable() {
    int cnt = 0;
    bool occur[16] = {false};
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (A[r][c] == 0) {
                Er = r;
                Ec = c;
            }
            else {
            	//printf(" cnt %d Er %d Ec %d  x %d\n",cnt,Er,Ec,A[r][c]);
                cnt += count(occur + 1, occur + A[r][c], false);
                occur[A[r][c]] = true;
            }
        }
    }
    //printf("Er %d Ec %d\n",Er,Ec);
    return (cnt + (Er + 1)) % 2 == 0;
}

int main() {
    int TC;
    scanf("%d", &TC);
    while (TC--) {
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                scanf("%d", &A[r][c]);
            }
        }

        path.clear();

        if (!solvable() || !IDAstar()) {
            puts("This puzzle is not solvable.");
        }
        else {
            for (int i = 0; i < path.size(); i++ ) {
                printf("%c", path[i]);
            }
            puts("");
        }
    }

    return 0;
}
