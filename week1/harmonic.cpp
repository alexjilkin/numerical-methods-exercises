#include <iostream>
#include <math.h>

float harmonic_series () {
  float sum = 0;

  for (int k = 1; k < 1000000000; k++) {
    sum += (1 / (float)k);
  }
  
  return sum;
}

int main() {
   
    std::cout << harmonic_series();

    std::cout << "\n";
}

