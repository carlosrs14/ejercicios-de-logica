#include <iostream>
using namespace std;
int main(){
    int n1, n2, lab, faltante;
    cout<<"Ingrese la nota número 1: ";
    cin>>n1;
    cout<<"Ingrese la nota número 2: ";
    cin>>n2;
    cout<<"Ingrese la nota del laboratorio: ";
    cin>>lab;

    faltante = 3*(60-lab*0.3)/0.7 - n1 - n2;
    cout<<"La nota que necesitas es: "<<faltante<<endl;

    return 0;
}