
#include <bits/stdc++.h>

using namespace std;
 
int main() {
	int t;
	scanf("%d", &t);
	while (t--) {
		int arr[15];
		for (int i = 0; i < 10; i++)
			scanf("%d", &arr[i]);
		int day[55][45] = {0};
		day[0][20] = 1;
		for (int i = 1; i < 51; i++) {
			for (int j = 1; j < 41; j++) {
				day[i][j] = arr[day[i - 1][j - 1] + day[i - 1][j] + day[i - 1][j + 1]];
				switch (day[i - 1][j]) {
					case 0 : printf(" "); break;
					case 1 : printf("."); break;
					case 2 : printf("x"); break;
					case 3 : printf("W"); break;
				}
			}
			printf("\n");
		}
		if (t)
			printf("\n");
	}
	return 0;
}
--------------------- 
??:??? 
??:CSDN 
??:https://blog.csdn.net/kl28978113/article/details/38302205 
????:?????????,?????????!
