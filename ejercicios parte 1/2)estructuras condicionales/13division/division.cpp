#include <iostream>
using namespace std;
int main(){
    int n1, n2;
    cout<<"Dividendo: ";
    cin>>n1;
    cout<<"Divisor: ";
    cin>>n2;
    if(n2==0){
        cout<<"No se puede dividir entre 0"<<endl;
        return 0;
    }
    if(n1%n2==0){
        cout<<"La división es exacta"<<endl;
    }else{
        cout<<"La división no es exacta"<<endl;
    }
    cout<<"Cociente: "<<n1/n2<<endl;
    cout<<"Resto: "<<n1%n2<<endl;
    return 0;
}