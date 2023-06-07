#include <iostream>
using namespace std;

int funcion(int n, int &ninv){
    
    ninv = ninv*10 + (n%10);
    
    if(n<10){
        return ninv;
    }else{
        return funcion(n/10, ninv);
    }
}

int main(){
    int numero=12345, numeroinv=0;
    funcion(numero, numeroinv);
    cout<<endl<<endl;
    cout<<numeroinv<<endl<<endl;
    return 0;
}