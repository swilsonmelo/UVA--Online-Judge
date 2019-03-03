#include <bits/stdc++.h>


using namespace std;


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int cases;
    char cad[100];
    scanf("%d",&cases);
    //printf("%d\n",cases);
    for(int i = 0; i < cases; i++){
        printf("Case %d\n",i+1);
        scanf("%s",&cad);
        map<char,int> dic;
        vector<char> pila;
        vector<char> res;
        int tam = 0;
        dic[cad[0]] = 0;
        //printf("%d\n",dic['A']);
        pila.push_back(cad[0]);
        res.push_back(cad[0]);
        for(int j = 1; j < strlen(cad); j++){
            char c = cad[j];
            if( dic.find(c) == dic.end() ){
                dic[c] = 1;
                res.push_back(c);
                tam += 1;
                pila.push_back(c);
            }
            else if( pila.size() > 0 ){

                    if( pila[pila.size()-1] == c ){
                        pila.pop_back();
                        if( pila.size() > 0 ){
                            dic[pila[pila.size()-1]] += 1;
                        }
                        else{
                            pila.push_back(c);
                        }
                    }
            }
        }
        sort(res.begin(),res.end());
        //printf("tam %d\n",tam);
        for(int k = 0; k < tam+1; k++){
            cout << res[k]<< " = " << dic[res[k]]<<endl;
        }

    }
    return 0;
}
