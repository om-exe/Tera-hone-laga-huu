#include<iostream.h>
#include<conio.h>
class a{
	public:
	a(){
		cout<<"Inside contructor";
	}

	~a(){
		cout<<"object destroyed";
	}



};
void main(){
	clrscr();
	a ob,obj;
	getch();
}