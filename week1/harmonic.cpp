#include <iostream>
#include <math.h>

float harmonic() {
  float sum = 0;
  float prevSum = 0;
  double k = 1;

  while(true) {
    sum += (1 / (float)k);

    if (sum == prevSum) {
      return sum;
      std::cout << k;
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

  while(true) {

    for (int j = 0; j < N; j++) {
      sum += (1 / (float)k);
    }

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
   
    std::cout << harmonic_bunch(50);

    std::cout << "\n";
}

