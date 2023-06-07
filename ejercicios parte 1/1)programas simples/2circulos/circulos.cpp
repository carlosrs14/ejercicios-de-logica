#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int radio;
    float perimetro, area;
    cout<<"Ingrese el radio del circulo: ";
    cin>>radio;
    perimetro = (float) 2 * M_PI * radio;
    area = (float) M_PI * radio * radio;
    cout<<"El perimetro es: "<<perimetro<<endl;
    cout<<"El area es: "<<area<<endl;
    return 0;
}