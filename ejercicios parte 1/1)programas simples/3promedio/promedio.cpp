#include <iostream>
using namespace std;
int main(){
    int n1, n2, n3, n4;
    float prom;
    cout<<"Ingrese la primera nota: ";
    cin>>n1;
    cout<<"Ingrese la segunda nota: ";
    cin>>n2;
    cout<<"Ingrese la tercera nota: ";
    cin>>n3;
    cout<<"Ingrese la cuarta nota: ";
    cin>>n3;
    prom= (float) (n1+n2+n3+n4)/4;
    cout<<"El promedio fue de: "<<prom<<endl;
    return 0;
}