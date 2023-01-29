#include <iostream>
#include <math.h>
#include <string>

#ifdef __APPLE__
  #include <Accelerate/Accelerate.h>
#endif

double * residual(int n, double **a, double *x, double *b, int m) {
  int c1 = n, ldb = n, pivot[n], info;
  int nrhs = 1;

  // Save original 
  memcpy(x, b, n * sizeof(double));

  // Solve the linear system
  dgesv_(&c1, &nrhs, &a[0][0], &c1, pivot, x, &ldb, &info);

  char no = 'N';
  double alpha = 1;
  double beta = 0;
  int incx = 1;
  double* y= new double[n];

  // Puts A * x into y
  dgemv_(&no, &c1, &c1, &alpha, &a[0][0], &n, b, &c1, &beta, y, &incx);

  if (info != 0) {
    std::cerr << "dgesv returned an error " << info << "\n";

    return b;
  } 

  
  std::cout << "x: [";

  for (int i = 0; i < n; i++)
    std::cout << x[i] << ", ";

  std::cout << "] \n";

  std::cout << "y: [";

  for (int i = 0; i < n; i++)
    std::cout << y[i] << ", ";

  std::cout << "] \n";

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
