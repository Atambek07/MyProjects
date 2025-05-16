#include <iostream>

unsigned long long ff(unsigned long long n) {
    unsigned long long result = 1;
    unsigned long long i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            result *= i;
            while (n % i == 0) {
                n /= i;
            }
        }
        i++;
    }
    result *= n;
    return result;
}

int main() {
    unsigned long long n;
    std::cin >> n;
    unsigned long long m = ff(n);
    std::cout << m << std::endl;
    return 0;
}
