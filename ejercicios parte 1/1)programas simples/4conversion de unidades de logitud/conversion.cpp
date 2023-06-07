#include <iostream>
using namespace std;

int main(){
    int cm;
    float in;
    cout<<"Ingrese la distancia en centimetros: ";
    cin>>cm;
    in = cm/2.54;
    cout<<"Tu distancia en pulgadas es: "<<in<<endl;
    return 0;
}