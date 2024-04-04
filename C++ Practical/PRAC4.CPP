#include<iostream.h>
#include<conio.h>
class A{
	public:
	void in(){
		cout<<"Hello ";
	}
};
class B:public A{
	public:
	void ou(){
		cout<<"Jevlis ka ";
	}
};
void main(){
	clrscr();
	B s;
	s.in();
	s.ou();
	getch();
}