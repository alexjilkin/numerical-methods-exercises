#include <iostream>
#include <math.h>
#include <string>

#ifdef __APPLE__
#include <Accelerate/Accelerate.h>
#endif

void print_vector(double *v, int n, std::string label);
void print_matrix(double **a, int n, std::string label);

// Returns the norm: ||Ax - b||_m
double residual(int n, double **a, double *x, double *b, int m)
{
  int incx = 1;
  char no = 'N';
  double alpha = 1.0, beta = 0;
  int one = 1;
  double y[n];
 
  print_vector(b, n, "b");
  print_vector(x, n, "x");

  print_matrix(a, n, "A");

  // Puts A * x into y
  dgemv_(&no, &n, &n, &alpha, a[0], &n, x, &incx, &beta, y, &incx);
  // dgemm_(&no, &no, &n, &one, &n, &alpha, &a[0][0], &n, x, &n, &beta, y, &n);
  print_vector(y, n, "y");
  // Residual vector
  double r[n];
  for (int i = 0; i < n; i++) {
    r[i] = y[i] - b[i];
  }

  print_vector(r, n, "r");

  double norm = 0;

  // Infinite norm
  if (m == 0) {
    double max = 0;
   

    for (int i = 0; i < n; i++)  {
       double current = abs(r[i]);
       if (current > max) {
        max = current;
       }
    }
      
    norm = max;
  } else {
    for (int i = 0; i < n; i++) 
      norm += pow(pow(abs(r[i]),m), 1/m);
  }


  return norm;
}

void residual_with_input()
{
  int n;
  // Reads matrix values
  std::cin >> n;
  std::cout << "n: " << n << "\n";
  
  double **a, **a_orig, b[n];

  // Initialize a 2d array as pointer
  a = new double *[n];  
  a_orig = new double *[n];

  for (int i = 0; i < n; i++)
    a[i] = new double[n];
  
  for (int i = 0; i < n; i++)
    a_orig[i] = new double[n];
  
  double temp;

  // Read 2D array into a and a_orig for a a duplicate
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      std::cin >> temp;

      a[j][i] = temp;
      a_orig[j][i] = temp;
    }
  }

  // Last n of inputs is the b array.
  for (int i = 0; i < n; i++)
  {
    double temp;
    std::cin >> temp;
    b[i] = temp;
  }

  double x[n];

  int p[n], info;
  int rhs = 1;

  // Move b into x variable
  memcpy(x, b, n * sizeof(double));

  // print_matrix(a, n, "A");
  
  // Solve the linear system
  dgesv_(&n, &rhs, &a[0][0], &n, p, x, &n, &info);

  // print_vector(x, n, "x");

  // dgesv_ transforms the 'a' given to it, so I created a copy named 'a_orig'
  double norm0 = residual(n, a_orig, x, b, 0);
  // double norm1 = residual(n, a_orig, x, b, 1);
  // double norm2 = residual(n, a_orig, x, b, 2);

  std::cout << 
    "The norms are: \n" << 
    "Infinite: " << norm0 << " " ;
    // "1: " << norm1 << " " <<
    // "2: " << norm2 << " " << "\n";
}

int main()
{
  residual_with_input();
}
