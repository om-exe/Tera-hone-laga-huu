#include<iostream.h>
#include<conio.h>
void main(){
	clrscr();
	int a;
	int *ptr;
	int **pptr;
	a=20;
	ptr=&a;
	pptr=&ptr;
	cout<<*ptr;
	cout<<**pptr;
	getch();
}