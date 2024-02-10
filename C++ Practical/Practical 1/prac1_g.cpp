#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    int a=25;
    float b= 11.46;
    cout<<setw<<a<<endl;
    cout<<setprecision(2)<<b<<endl;
    cout<<setfill('$')<<setw(10)<<a;
    return 0;
}