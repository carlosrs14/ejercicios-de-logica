#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

bool isDivisible(int dividen, int divider) {
    return dividen % divider == 0;
}
bool isPrime(int x) {
    for (int i = 2; i <= x / 2; i++) {
        if (isDivisible(x, i))
            return false;
    }
    return true;
}
int iPrime(int iEsim) {
    int count = 0, i = 2, prime = 0;
    do{
        if(isPrime(i++)){
            count++;
            prime = i - 1;
        }
    } while (count < iEsim);
    return prime;
}
vector<int> firstsPrimes(int n) {
    vector<int> primes;
    int i = 2;
    while ((int) primes.size() != n) {
        if (isPrime(i))
            primes.push_back(i);
        i++;
    }
    return primes;
}
vector<int> primesUntil(int x) {
    vector<int> primes;
    for (int i = 2; i <= x; i++) {
        if(isPrime(i)) {
            primes.push_back(i);
        }
    }
    return primes;
}
vector<int> firstsPrimesMersenne(int n) {
    vector<int> primes = firstsPrimes(n);
    vector<int> primesMersenne;
    for (int i = 0; i < primes.size(); i++) {
        primesMersenne.push_back(pow(2, primes.at(i)) - 1);
    }
    return primesMersenne;
}
int main() {
    vector<int> aux = firstsPrimesMersenne(6);
    for (int i = 0; i < aux.size(); i++) {
        cout << "[" << aux.at(i) << "]";
    }
    cout << endl;
    cout<< pow(2, 13) << endl;;
    cout << iPrime(1) << endl;
    return 0;
}