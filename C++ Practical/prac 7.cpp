#include<iostream.h>
#include<conio.h>
class Base{
    public:
    void disp(){
        cout<<"Base class";
    }

};
class child:public Base{
    public:
    void disp(){
        cout<<"derived class";
    }
};
int main(){
    getch()
    Base d;
    child b;
    b.disp()
    d.disp()
}