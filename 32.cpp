#include <iostream>
#include <algorithm>
#include <list>
#include <chrono>

int main() {
    std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();
    int digits[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int multiplicand1, multiplicand2, multiplier1, multiplier2, product, sum = 0;
    std::list<int> products;
    do {
        multiplicand1 = digits[0];
        multiplicand2 = multiplicand1 * 10 + digits[1];
        multiplier2 = digits[2] * 100 + digits[3] * 10 + digits[4];
        multiplier1 = multiplier2 + digits[1] * 1000;
        product = digits[5] * 1000 + digits[6] * 100 + digits[7] * 10 + digits[8];
        if (multiplicand1 * multiplier1 == product || multiplicand2 * multiplier2 == product) {
            if(std::find(products.begin(), products.end(), product) == products.end()) {
                sum += product;
                products.push_back(product);
            }
        }
    } while (std::next_permutation(digits, digits + 9));
    std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
    std::cout << sum << std::endl;
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>( t2 - t1 ).count();
    std::cout << "Time elapsed: " << duration << " miliseconds" << std::endl;

    return 0;
}

