#include <iostream>
#include <cmath>

void funks(double x) {
    std::cout << "\n";
    double f1 = ((cos(x) - 1) / (x * x));
    double f2 = (exp(x) - exp(-x)) / 2*x;
    std::cout << "f1: " + std::to_string(f1) + " f2: " + std::to_string(f1) + "\n";
}

int main() {
    double x;
    while(true) {
        std::cout << "Insert number:";
        std::cin >> x;
        std::cout << "\n";
       
        funks(x);
        
    }
}