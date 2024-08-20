#include <iostream>

using namespace std;

int invertNumber(int x) {
    int inverted =  0;
    while(x > 0) {
        inverted = (inverted * 10) + x % 10;
        x = x / 10;
    }
    return inverted;
}
bool isPalindrome(int x) {
    return x == invertNumber(x);
}
int main() {
    int i = 0;
    cout << isPalindrome(81418) << endl;
    return 0;
}