#include<iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
    cin.tie(NULL);
    int n,m;
    cin >>n>>m;
    int list[m];
    for(int i=0;i<m;i++){
        cin >>list[i];
    }

    int t;
    cin>>t;
    while(t--){
        int y1,x1,y2,x2,s;
        cin >>y1 >>x1 >>y2 >>x2 >>s;
        if ((x2-x1)%s!=0 ||(y2-y1)%s!=0){
            cout<<"No"<<endl;
        }else{
            int height=y1+floor((n-y1)/s)*s;
            string answer="YES";
            int a,b;
            int* max;
            a=fmin(x1,x2);
            b=fmax(x1,x2);
            if(height<=*max_element(list+a-1,list+b-1)){
                answer="NO";
            }
            cout<<answer<<endl;
        }
    }
}