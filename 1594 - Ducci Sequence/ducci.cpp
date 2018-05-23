#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>



using namespace std;

const int maxn = 101;
int t,n,a[maxn];
int b[maxn]= {0};
int c[maxn]= {0};


void seq(int a[])
{
    for(int i=1; i<=n; ++i)
    {
        a[i]=abs(a[i]-a[i+1]);
    }
    a[n+1]=a[1];
}

bool comp(int a[], int b[])
{
    for(int i=1; i<=n; ++i)
    {
        if(a[i]!=b[i])  return false;
    }
    return true;
}

int main()
{
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i=1; i<=n; ++i)
        {
            scanf("%d", &a[i]);
            b[i]=a[i];
        }
        a[n+1]=b[n+1]=a[1];
        bool loop =true;
        for(int i=0; i<1010; ++i)
        {
            seq(a);
            seq(b);
            seq(b);
            if(comp(a,c))
            {
                loop = false;
                break;
            }
            if(comp(a,b))
            {
                loop = true;
                break;
            }
            if(comp(b,c))
            {
                loop = false;
                break;
            }
        }
        if(loop)    printf("LOOP\n");
        else printf("ZERO\n");
    }
}
