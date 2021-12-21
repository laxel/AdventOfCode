#include <stdlib.h>
#include <chrono>

#include"d01/d01.h"

using namespace std::chrono;

int main() {
    string res [2];

    // === Day 1 ===
    auto start = high_resolution_clock::now();
    day01(res, "d01/input.txt");
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start); 
    cout << "< Day01 > " << "P1: " << res[0] << "\tP2: " << res[1] << 
        "\tTime: " << duration.count() << "us\n"; 





    return 0;
}