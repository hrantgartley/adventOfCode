#include <cstddef>
#include <fstream>
#include <iostream>
#include <sstream>

size_t customHash(std::string str) {
    size_t value = 0;
    for (int i = 0; i < str.length(); i++) {
        value += (int)str[i];
        value *= 17;
        value %= 256;
    }
    return value;
}

int main() {
    std::ifstream inputFile("input");
    if (!inputFile.is_open()) {
        std::cout << "Could not open file!" << std::endl;
        return 1;
    }

    std::string line;
    size_t totalHash = 0;

    while (std::getline(inputFile, line)) {
        std::stringstream ss(line);
        std::string token;

        while (std::getline(ss, token, ',')) {
            totalHash += customHash(token);
        }
    }

    inputFile.close();

    std::cout << "Sum of hashed values: " << totalHash << std::endl;

    return 0;
}
