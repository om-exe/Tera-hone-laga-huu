#include<iostream>
using namespace std;
int main(){
    cout<<"Enter your elements  ";
    int i,a[3];
    for (int i = 0; i < 3; i++)
    {
        cin>>a[i];
        cout<<a<<endl;
    }
    cout<<"Single dimenstional array is:\n";
    for (int i = 0; i < 3; i++)
    {
        cout<<a[i]<<",";
    }
    

    
    return 0;
}       