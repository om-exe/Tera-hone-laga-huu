#include<iostream.h>
#include<conio.h>
class Yasha;
class Gargi{
    private:
    int money = 10;
    friend void Om(Gargi,Yasha);
};
class Yasha{
    private:
    int money = 20;
    friend void Om(Gargi,Yasha);
};
void Om(Gargi g ,Yasha y){
    cout<<"Money given by yasha "<<y.money;
    cout<<"Money given by gargi "<<g.money;
};
int main(){
    clrscr();
    Gargi obj1;
    Yasha obj2;
    Om(obj1,obj2);
    return 0;
    getch();
}
