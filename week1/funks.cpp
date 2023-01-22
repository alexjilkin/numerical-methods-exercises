#include <iostream>
#include <cmath>

double factorial(double n)
{
    double f = 1;
    for (double i = 1; i <= n; ++i)
        f *= i;
    return f;
}

double cos_taylor(double x, double k) {
    double sum = 0;

    for (double n = 1; n < k; n++) {
        sum += (pow(-1, n) * pow(x, (2 * n) - 2)) / factorial(2 * n);
    }
    
    return sum;
}

// Taylor series of e^x - e^-x
double exp_taylor(double x, double k) {
    double sum = 0;

    for (double n = 1; n < k; n++) {
        sum += pow(x, (2 * n) - 2) / factorial((2 * n) - 1);
    }
    
    return sum;
}


void funks(double x) {
    double f1 = (cos(x) - 1) / (x * x);
    double f2 = (exp(x) - exp(-x)) / (2 * x);
    
    std::cout << "f1: " + std::to_string(f1) + " f2: " + std::to_string(f2) + "\n";
}

void funks_Taylor(double x) {
    double f1 = cos_taylor(x, 1000);
    double f2 = (exp_taylor(x, 1000));
    
    std::cout << "f1: " + std::to_string(f1) + " f2: " + std::to_string(f2) + "\n";
}

int main() {
    double x;
    while(true) {
        std::cout << "Insert number:";
        std::cin >> x;

        std::cout << "funks - ";
        funks(x);

        std::cout << "funks_Taylor - ";
        funks_Taylor(x);
    }
}