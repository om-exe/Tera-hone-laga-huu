#include<iostream>
using namespace std;
int notes()
{
  /*
    
    Base on scope, variables can be classified into two types:

    1.Local variables
    2.Global variables


    Local variables:
    Local variables are declared inside the braces of any function and can be assessed only from there. 

    Global variables:
    Global variables are declared outside any function and can be accessed from anywhere

    **************************Data Types******************************
    Data types define the type of data that a variable can hold; for example, an integer variable can hold integer data, a character can hold character data, etc.

    Data_type Variable_name = Value;--------> Syntax
    Ex: int a=4; -----> Example
    Data types in C++ are categorized into three groups:

        Built-in
        User-defined
        Derived
    1. Built-in Data Types in C++:
       A. Int
       B.Float
       C.Char
       D.Double
       E.Boolean
    2. User-Defined Data Types in C++:
       A.Struct
       B.Union
       C.Enum
    3. Derived Data Types in C++:
       A.Array
       B.Pointer
       C.Function

    */
 return 0;   
}
int a  = 25;  //-----------> Global Variable
int main()
{
    int a = 12;   //----------------> Local Variable
    cout<<"The value of a is "<<a<<endl;
    // Scope resolution Operator --> ::
    cout<<"The value of a is "<<::a<<endl;//-------------->  [::] Use to access the Global variable

    return 0; 
}


