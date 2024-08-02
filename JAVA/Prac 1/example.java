class Example{
    int a,b;    // Instance Variables

// Constructor overloading 
public Example(){
    this.a=0;
    this.b=0;
    System.out.println(" Default Constructor : a  = "+a+" b = "+b);

} 
public Example(int a){
    this.a=0;
    this.b=0;
    System.out.println(" Single Parameter Constructor : a  = "+a+" b = "+b);

} 
public Example(int a,int b ){
    this.a=0;
    this.b=0;
    System.out.println(" Two  Parameter Constructor : a  = "+a+" b = "+b);

} 

// Method Overloading
public void display(){
    System.out.println(" Display with no Parameter  : a  = "+a+" b = "+b);
}

public void display(int a){
    System.out.println(" Display with one Parameter  : a  = "+a+" b = "+b);
}
public void display(int a ,int b){
    System.out.println(" Display with two Parameter  : a  = "+a+" b = "+b);
}

//Static method

public static void staticMethod()
{
    System.out.println("This is Static Method ");
}

public static void main(String[] args){
    // Constructor Overloading 
    Example obj1 = new Example();
    Example obj2 = new Example(5);
    Example obj3 = new Example(5,10);

    //  Method Overloading examples 
    obj1.display();
    obj2.display(7);
    obj3.display(7,14);

    //Static method example
    Example.staticMethod();
}
}