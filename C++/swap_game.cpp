#include<bits/stdc++.h>
#define ll long long


using namespace std;

int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;

        ll f;
        cin>>f;
        ll first =f;
        ll min_n = f;
        n--;
        while(n--){
            cin>>f;
            min_n = min(f,min_n);
        }
        if(min_n==first){
            cout<<"Bob"<<endl;
        }
        else cout<<"Alice"<<endl;
    }
}
