#include <iostream>

int main()
{
    int v1, v2 = 0;
    
    std::cout << "enter two numbers" << std::endl;
    std::cin >> v1 >> v2;

    int lower = v1;
    int upper = v2;

    if (v1 > v2)
    {
        upper = v1;
        lower = v2;
    }

    while (lower <= upper)
    {
        std::cout << lower << std::endl;
        ++lower;
    }
}