#include <iostream>
#include <climits>
#include <math.h>

float harmonic_kahan(double N) {
  float s,x,y,t,e;

  s = 1;
  e = 0.0;

  for (long int i = 2; i <= N; i++) {
    
    x = 1.0 / (float)i;
    y = x - e;
    t = s + y;
    e = (t - s) - y;

    if (i % 100000000 == 0) {
       std::cout << i;
       std::cout << "\n";

       std::cout << e;
       std::cout << "\n";
       std::cout << y;
       std::cout << "\n";

       std::cout << s;
       std::cout << "\n";
    }
    s = t;
  }

  return s;
}

int main() {
  std::cout << harmonic_kahan(1000000000000);
  std::cout << "\n";
}