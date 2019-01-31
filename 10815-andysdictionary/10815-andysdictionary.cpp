#include <bits/stdc++.h>
using namespace std;

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
    string s;
    set<string> st;
    set<string>:: iterator it;
    while(cin>>s)
    {
        string ss="";
        if(s=="0") break;
        for(int i=0; i<s.size(); i++)
        {
            char c=tolower(s[i]);
            if(c>=97&&c<=122)
                ss += c;
            else if (ss != "")
            {
                st.insert(ss);
                ss = "";
            }

        }
        if(ss!="")
            st.insert(ss);
    }
    for(it=st.begin(); it!=st.end(); it++)
    {
        cout<<*it<<endl;
    }
    return 0;
}
