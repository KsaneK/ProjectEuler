#include <iostream>
#include <fstream>
#include <chrono>
#include <map>

using namespace std;

int matrix[80][80];
int memory[80][80];

unsigned int min_two_ways(int matrix[80][80], int row, int column) {
    if (memory[row][column] != 0) {
        return memory[row][column];
    }
    int result;
    if (row < 79 and column < 79) {
        result = matrix[row][column] + min(min_two_ways(matrix, row + 1, column), min_two_ways(matrix, row, column + 1));
    } else if (row < 79) {
        result = matrix[row][column] + min_two_ways(matrix, row + 1, column);
    } else if (column < 79) {
        result = matrix[row][column] + min_two_ways(matrix, row, column + 1);
    } else {
        result = matrix[row][column];
    }
    memory[row][column] = result;
    return result;
}

int main() {
    ifstream file { "data" };
    for(int i = 0; i < 80; i++) {
        for(int j = 0; j < 80; j++) {
            file >> matrix[i][j];
        }
    }

    chrono::high_resolution_clock::time_point start = chrono::high_resolution_clock::now();
    unsigned int result = min_two_ways(matrix, 0, 0);
    chrono::high_resolution_clock::time_point stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start).count();
    cout << "Result: " << result << endl;
    cout << "Time elapsed: " << duration << "microseconds." << endl;
    return 0;
}
