#include <iostream>
#include <math.h>
#include <string>

#ifdef __APPLE__
  #include <Accelerate/Accelerate.h>
#endif

double * residual(int n, double **a, double *x, double *b, int m) {
  int c1 = n, ldb = n, pivot[n], info;
  int nrhs = 1;

  // Solve the linear system
  dgesv_(&c1, &nrhs, &a[0][0], &c1, pivot, b, &ldb, &info);

  if (info == 0) {
    std::cout << "b: [";

    for (int i = 0; i < n; i++)
      std::cout << b[i] << ", ";

    std::cout << "] \n";
  } else {
    std::cerr << "dgesv returned an error " << info << "\n";
  }

  return b;
}

double * residual_with_input() {
  int n;

  // Reads matrix values
  std::cout << "Enter n and then on each line type a row of the matrix A. followed by a line of b: \n";
  std::cin >> n;
  std::cout << "";


  double **a, b[n];

  // Initialize a 2d array as pointer
  a = new double *[n];
  for(int i = 0; i <n; i++)
    a[i] = new double[n];

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++)
      std::cin >> a[j][i];
  }

  for (int i = 0; i < n; i++) {
    std::cin >> b[i];
  }

  double x[5] = {1, 2, 3, 4, 5};

  residual(n, a, &x[0], &b[0], 1);

}


int main()
{
  residual_with_input();
}
