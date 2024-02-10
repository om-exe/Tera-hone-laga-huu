#include<iostream>
using namespace std;

int main() {
    int i, j, a[3][3];
    cout << "Elements of the array are:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> a[i][j];
        }
        cout << endl;
    }
    cout << "Array elements are:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << a[i][j] << ",";
        }
        cout << endl;
    }
    return 0;
}
