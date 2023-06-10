#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int A,B;
    float C;

    cout<<"Ingrese el cateto A: ";
    cin>>A;
    cout<<"Ingrese el cateto B: ";
    cin>>B;
    C= sqrt(A*A + B*B);
    cout<<"La hipotenusa de este triangulo es:  "<<C<<endl;

    return 0;
}