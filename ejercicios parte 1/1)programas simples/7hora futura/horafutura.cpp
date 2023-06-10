#include <iostream>
using namespace std;
int main(){
    int h_act, aumento, h_fut;

    cout<<"Hora actual: ";
    cin>>h_act;
    cout<<"Cantidad de horas: ";
    cin>>aumento;
    h_fut = (h_act+aumento) % 12;
    
    cout<<"La hora futura será: "<<h_fut<<endl;
    return 0;
}