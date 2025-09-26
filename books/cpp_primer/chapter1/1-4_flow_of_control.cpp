#include <iostream>

int main()
{
    int sum = 0, val = 1;

    while (val <= 10) {
        sum += val;
        ++val;
    }
    std::cout << "Sum of 1 to 10 inclusive is "
              << sum << std::endl;

    return 0;
}

int for_loop() 
{
    int sum = 0;
    for (int val = 1; val <= 10; ++val) // notice we dont need curly brackets for a single line
        sum += val;

        // val = 2; this will yield an error, because val is not defined outside of our for loop, which currently only evaluates that first line
        // we could use brackets instead to include multiple lines

    std::cout << "Sum of 1 to 10 inclusive is "
            << sum << std::endl;
    
    return 0;
}

int read_until_eof()
{
    int sum = 0, value = 0;
    
    while (std::cin >> value)
        sum += value;
    
    std::cout << "Sum is: " << sum << std::endl;
    return 0;    
}