#include <bits/stdc++.h>

using namespace std;

int main(){
	
	int cases,n;
	
	scanf("%d",&cases);
	while(cases--){	
		char name[1000];
		gets(name);	
		//getline(cin,name);
		
		char * spliter;
		spliter = strtok(name," ");
		while(spliter != NULL){
			cout << spliter << "\n"	;
			spliter = strtok(NULL," ");
		}
		//cout << name << "\n"	;
	}	
		
		
	return 0;
}
