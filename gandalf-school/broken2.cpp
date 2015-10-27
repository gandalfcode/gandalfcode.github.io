#include <iostream>

int ComputeFactorial(int number) {
  int fact = 0;

  for (int j = 1; j <= number; j++) {
    fact = fact * j;
  }

  return fact;
}

int main() {
  int input;
  std::cout<< "Enter a number to compute its factorial" << std::endl;
  std::cin >> input;

  int fac = ComputeFactorial(input);
  std::cout << "The result is " << fac << std::endl;
}