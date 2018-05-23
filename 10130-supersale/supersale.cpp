#include<stdio.h>
#include<string.h>


const int  max = 1000;
int mat[max][max];

int  armador(int v[],int w[],int n,int W)
{
    
    for(int i=0; i<=W; i++)
    {
        mat[0][i]=0;
    }
    for(int i=1; i<=n; i++)
    {
        for(int j=0; j<=W; j++)
        {
            if(w[i]<=j)
            {
                int p= mat[i-1][j];
                int q=v[i]+mat[i-1][j-w[i]];
                if(p>q)
                {
                    mat[i][j]=p;
                }
                else
                {
                    mat[i][j]=q;
                }
            }
            else
            {
                mat[i][j]=mat[i-1][j];
            }
        }
    }

    return mat[n][W] ;
}
int main()
{
    int n,v[max],w[max],t,caso,usuarios,m;
    scanf("%d",&caso);
    while(caso--)
    {

        scanf("%d",&n);

        for(int i=1; i<=n; i++)
        {
            scanf("%d %d",&v[i],&w[i]);
        }
        t=0;

        scanf("%d",&usuarios);
        for(int i=1;i<=usuarios;i++)
        {
            scanf("%d",&m);
            t+=armador(v,w,n,m);
        }
        printf("%d\n",t);
    }

}
