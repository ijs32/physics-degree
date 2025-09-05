#include <iostream>
#include <vector>

using namespace std;

double square(int x)
{
  return x * x;
}

int main()
{
  int x = 4;
  int y = 2;

  cout << "The square of " << x << " is " << square(x);

  x += y; // x = x+y
  ++x;    // increment: x = x+1
  x -= y; // x = x-y
  --x;    // decrement: x = x-1
  x *= y; // scaling: x = x*y
  x /= y; // scaling: x = x/y
  x %= y; // x = x%y
}

// function overloading, you can have multiple functions of the same name but accepting different types
void print(int x);
void print(double x);
void print(string x);

void user()
{
  print(42);
  print(42.53);
  print("D is for Digital");
}

vector<int> vec = {1, 2, 3, 4, 5};

// we can let the initizializer choose a variable type for us
auto b = true; // a bool
auto ch = 'x'; // a char
auto i = 123;  // an int
auto d = 1.2;  // a double
auto y = 2;
auto z = sqrt(y); // z has the type of whatever sqrt(y) returns
auto x = 1;
