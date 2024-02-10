#include <iostream> 
using namespace std; 

int main() 
{ 
	int num, test = 40; 
	num = test < 10 ? 10 : test + 10; 
	cout<<("Num - Test = %d", num - test); 

	return 0; 
}
