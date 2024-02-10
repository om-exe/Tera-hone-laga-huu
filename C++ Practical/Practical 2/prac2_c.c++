#include<iostream>
using namespace std;
int main(){
    char n;
    cout<<"Enter alphabetical ";
    cin>>n;
    switch (n)
    {
    case 'i':
        cout<<"i is vowel";
        break;
    case 'c':
        cout<<"c is vowel";
        break;
    case 'o':
        cout<<"o is vowel";
        break;
    case 'v':
        cout<<"v is vowel";
        break;
    case 'e':
        cout<<"e is vowel";
        break;  
    case 'a':
        cout<<"a is vowel";
        break;  
    default:
        cout<<n<<"is consonent";
        break;
    }
    return 0;
}