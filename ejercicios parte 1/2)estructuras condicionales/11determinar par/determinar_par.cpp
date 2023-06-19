#include <iostream>
using namespace std;
int main(){
    int num;
    cout<<"Ingrese un número: ";
    cin>>num;

    if(num%2==0){
        cout<<"Es un número par"<<endl;
    }else{
        cout<<"Es un número impar"<<endl;
    }
}