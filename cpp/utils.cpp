#include <fstream>
#include <sstream>
#include <string>
#include <filesystem>
#include <iostream>
#include <vector>


namespace utils{
    std::string readFileContents(const std::string& filePath) {
        std::ifstream fileStream(filePath);
        if (!fileStream) {
            std::cerr << "Failed to open file: " << filePath << std::endl;
            return {""};
        }
        std::stringstream buffer;
        buffer << fileStream.rdbuf();
        return buffer.str();
    }
}
