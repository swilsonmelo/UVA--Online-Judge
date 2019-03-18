#include <bits/stdc++.h>
using namespace std;
#define maxn 210
#define maxw 210

int dp[maxn][maxw];
int weight[maxn];
char arr[600];
int n;
int sol(int cur, int left)
{
    //cout << cur << " "<<left<< endl;
    if (dp[cur][left] != -1)
        return dp[cur][left];
    int m = 0, t;
    for (int i = cur; i < n; i++)
    {
        if (weight[i] <= left)
        {
            //cout<<i<<endl;
            t = weight[i] + sol(i + 1, left - weight[i]);

            if (m < t)
                m = t;
        }
    }
    dp[cur][left] = m;
    //cout << "res "<< cur <<" "<<left <<" "<<dp[cur][left] << endl;
    return dp[cur][left];
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out2.txt", "w", stdout);
    int i, j, len, test, k, temp, sum;
    scanf("%d", &test);
    getchar();
    while (test--)
    {
        gets(arr);
        len = strlen(arr);
        i = j = sum = 0;
        while (i < len)
        {
            temp = 0;
            while (arr[i] >= '0' && arr[i] <= '9')
            {
                temp = temp * 10 + (arr[i] - '0');
                i++;
            }
            //cout << temp << endl ;
            weight[j++] = temp;
            sum += temp;
            i++;
        }

        if (sum % 2 == 1)
        {
            printf("NO\n");
            continue;
        }
        n = j;
        memset(dp, -1, sizeof dp);
        int ans = sol(0, sum / 2);
        //printf("%d \n", sum/2);
        /*  for ( i =  0 ; i < n ; i++){
      for ( j = 0; j < sum/2 ; j++)
      cout << dp[i][j] << " ";
      cout<<endl;
  }*/
        if (ans == sum / 2)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }

    return 0;
}