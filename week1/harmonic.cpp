#include <iostream>
#include <math.h>

float harmonic() {
  float sum = 0;
  float prevSum = 0;
  double k = 1;

  // Sums up the harmonic series until the sum stops changing
  while(true) {
    sum += (1 / (float)k);

    if (sum == prevSum) {
      return sum;
    }

    prevSum = sum;
    k++;
  }
  
  return -1;
}

float harmonic_bunch (int N) {
  float sum = 0;
  float prevSum = 0;
  double k = 1;

  // Sums up the harmonic series in bunches of N until the sum stops changing
  while(true) {

    float innerSum = 0;

    for (int j = 1; j <= N; j++) {
      innerSum += (1 / (float)(((k - 1) * N) + j));
    }

    sum += innerSum;

    if (sum == prevSum) {
      return sum;
      std::cout << k;
    }

    prevSum = sum;
    k++;
  }
  
  return -1;
}



int main() {

    std::cout << "harmonic(): ";
    std::cout << harmonic();
    
    std::cout << "\n";
    std::cout << "harmonic_bunch(50): ";
    std::cout << harmonic_bunch(50);
    std::cout << "\n";

    std::cout << "harmonic_bunch(100): ";
    std::cout << harmonic_bunch(100);

    std::cout << "\n";
    std::cout << "harmonic_bunch(200): ";
    std::cout << harmonic_bunch(200);

    std::cout << "\n";
    std::cout << "harmonic_bunch(500): ";
    std::cout << harmonic_bunch(500);
    std::cout << "\n";
}

