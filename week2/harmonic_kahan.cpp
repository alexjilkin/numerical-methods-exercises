#include <iostream>
#include <climits>
#include <math.h>

// To run it: 'make kahan/build kahan/run'
// Returns the harmonic series upto N if kahan summation
float harmonic_kahan(double N) {
  float s,x,y,t,e;

  s = 1;
  e = 0.0;

  for (long int i = 2; i <= N; i++) {
    
    x = 1.0 / (float)i;
    y = x - e;
    t = s + y;
    e = (t - s) - y;

    s = t;
  }

  return s;
}

int main() {
  std::cout << harmonic_kahan(300000000);
  std::cout << "\n";
}