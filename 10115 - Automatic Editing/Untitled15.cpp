#include<bits/stdc++.h>

//414 Machined Surfaces
using namespace std;

int N;
int a[20],Max = 0;
char line[30];
int ans;

int main()
{
    //freopen ("414.in","r",stdin);
    while(scanf("%d",&N),N)
    {
        ans=0,Max=0;
        memset(a,0,sizeof(a));
        memset(line,0,sizeof(line));
        getchar();
        for (int i=0; i<N; i++)
        {
            gets(line);
            for (int j=0; line[j]; j++)
                if (line[j]=='X')
                    a[i]++;
            if (a[i]>Max)
                Max = a[i];
        }
        for (int i=0; i<N; i++)
            ans += (Max-a[i]);
        printf("%d\n",ans);
    }
    return 0;
}

