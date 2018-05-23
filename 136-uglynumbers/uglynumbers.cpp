#include<stdio.h>
#include<string.h>
#include<bits/stdc++.h>

using namespace std;

int pos2 = 0;
int pos3 = 0;
int pos4 = 0;

int vec[1500];



void armador(){
	vec[0]=1;
	for(int i = 1; i < 1500; i++){
		vec[i] = min(2*vec[pos2],min(3*vec[pos3],5*vec[pos4]));
		if(vec[i]==2*vec[pos2]){
			pos2 += 1;
		}
		if(vec[i]==3*vec[pos3]){
			pos3 += 1;
		}
		if(vec[i]==5*vec[pos4]){
			pos4 += 1;
		}
		
	}
	
}

int main(){
	armador();
	printf("The 1500'th ugly number is %d.\n",vec[1499]);
	return 0;
}

