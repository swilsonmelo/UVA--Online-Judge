#include<bits/stdc++.h>


using namespace std;

char s1[105], s2[105];
char ch[105],str[2][105];
int main(){

	int n;
	scanf("%d",&n);
	getchar();
	while(n--)
	{
		gets(s1);
		gets(s2);
		int len1 = strlen(s1);
		int len2 = strlen(s2);
		int k = 0;
		int x[2], y[2];
		int count = 0;
		memset(ch,0,sizeof(ch));
		memset(str,0,sizeof(str));
		
		for(int i = 0; i < len1; i++)
		{
			if(s1[i] == '<')
			{
				count++;
				x[count-1] = i;
				
				for(int j = i+1; j < len1; j++)
				{
					if(s1[j] != '>')
					{
						ch[k++] = s1[j];
					}
					else
					{
						y[count-1] = j;
						strcpy(str[count-1],ch);
						memset(ch,0,sizeof(ch));
						k = 0;
						break;
					}
				}
			}
		}
		for(int i = 0; i < len1; i++)
		{
			if(s1[i] == '<' || s1[i] == '>')
				continue;
			printf("%c",s1[i]);
		}
		printf("\n");
		for(int i = 0; i < len2; i++)
		{
			if(s2[i] != '.')
			{
				printf("%c",s2[i]);
			}
			else
			{
				break;
			}
		}
		printf("%s",str[1]);
		for(int j = y[0]+1; j < x[1]; j++)
		{
			printf("%c",s1[j]);
		}
		printf("%s",str[0]);
		for(int k = y[1]+1; k < len1; k++)
		{
			printf("%c",s1[k]);
		}
		printf("\n");
	}
	return 0;
}
