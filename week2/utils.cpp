#include <iostream>
#include <string>

void print_vector(double *v, int n, std::string label)
{
  std::cout << label << ": [";

  for (int i = 0; i < n; i++)
    std::cout << v[i] << ", ";

  std::cout << "] \n";
}

void print_matrix(double **a, int n, std::string label)
{
  std::cout << label << ": ";

  for (int i = 0; i < n; i++)
  {
    std::cout << "\n";

    for (int j = 0; j < n; j++)
      std::cout << a[j][i] << ", ";
  }

  std::cout << " \n";
}