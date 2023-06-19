#include <iostream>
using namespace std;
int main(){
    int anio; bool verificar=false;;
    cout<<"Ingrese el año: ";
    cin>>anio;
    if(anio%4==0)
        verificar=true;
    if(anio>=1582){
        if(anio % 100 == 0){
            verificar=false;
            if(anio % 400 == 0){
                verificar = true;
            }
        }

    }
    
    if(verificar){
        cout<<"El año es bisiesto"<<endl;
    }else{
        cout<<"El año NO es bisiesto"<<endl;
    }
    return 0;
}