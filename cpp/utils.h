//
// Created by Marcelo Duarte Trevisani on 05/12/2023.
//

#ifndef UTILS_H
#define UTILS_H

#include <string>

namespace utils{
    std::string readFileContents(const std::string& filePath);
    std::vector<std::string> splitString(const std::string& line, char delimiter);
}

#endif //UTILS_H
