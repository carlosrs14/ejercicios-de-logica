#include <iostream>
using namespace std;
int main(){
    float numero;
    int numeroInt;

    cout<<"Ingrese un número: ";
    cin>>numero;
    
    numeroInt = numero;
    numero = numero - numeroInt;

    cout<<"Decimal: "<<numero<<endl;
    return 0;
}