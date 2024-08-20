#include <iostream>

using namespace std;

bool isEven(int x) {
    return x % 2 == 0;
}
int main() {
    cout << isEven(-10) << endl;
    return 0;
}