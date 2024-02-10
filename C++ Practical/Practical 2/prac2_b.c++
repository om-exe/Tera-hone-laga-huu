#include <iostream>
using namespace std;
int main()
{
    int a, b, c;
    cout << "Enter the Number";
    cin >> a >> b >> c;
    if (a > b || b >> c)
    {
        cout << "A is greater" << a;
    }
    else if (c > a && b > c);
    {
        cout << "B is greater " << b;
    }
    else
    {
        cout << "c is greater " << c;
    }
    return 0;
}