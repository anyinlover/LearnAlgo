#include <iostream>
#include <algorithm>
#include <vector>

int main(int, char**) {
    std::vector<int> vec = {1,5,9,4,3};
    std::sort(vec.begin(), vec.end());
    std::cout << vec.back() << std::endl;
    return 0;
}
