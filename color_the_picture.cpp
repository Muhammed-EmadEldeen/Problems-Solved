#include<iostream>
#define ll long long
 
using namespace std;
 
int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n,m,k;
        cin>>n>>m>>k;
        ll columns1 =m;
        ll columns2 =n;
        bool odd_problem_1=true;
        bool odd_problem_2=true;
        while(k--){
            ll number;
            cin>>number;
            ll columns=number/n;
            if (columns>2){
                columns1-=columns;
                odd_problem_1=false;            
            }elif (columns==2) columns1-=columns;
            ll columns22=number/m;
            if (columns2>2){
                columns2-=columns22;
                odd_problem_2=false;
            }elif(columns==2) columns2-=columns22;
        }
       
        
        if((maximum>0 || odd_problem_1 )&& (reverse2>0 || odd_problem_2)) cout<<"No"<<endl;
        else cout <<"Yes"<<endl;
 
    }
 
}