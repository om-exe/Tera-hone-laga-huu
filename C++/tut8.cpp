#include<iostream>
#include <iomanip>
using namespace std;
int main()
{
    // Constants in C++
    // Constants are unchangeable; when a constant variable is initialized in a program, its value cannot be changed afterwards.
    // const int a = 45;
    // cout<<"The value of a is: "<<a;
    // int a = 20;  This gives an error as 'a' is defined as constant

    // In C++ programming, language manipulators are used in the formatting of output. The two most commonly used manipulators are: "endl" and "setw".
    // "endl" is used for the next line.
    // "setw" is used to specify the width of the output.
    int x = 15;
    int  y = 45;
    int z = 488;
    cout<<"The value of x without setw and endl:  "<<x;
    cout<<"The value of y without setw and endl:  "<<y;
    cout<<"The value of z without setw and endl:  "<<z;
    cout<<"*****************";

    cout<<"The value of x with setw and endl:"<<setw(4)<<x<<endl;
    cout<<"The value of y with setw and endl:"<<setw(4)<<y<<endl;
    cout<<"The value of z with setw and endl:"<<setw(4)<<z<<endl;

    // Operator Precedence & Operator Associativity
    // Operator precedence helps us to solve an expression
    // We can see this
    // https://en.cppreference.com/w/cpp/language/operator_precedence

}