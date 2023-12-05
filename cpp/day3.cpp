#include "day3.h"

#include <cctype>
#include <string>
#include <sstream>
#include <iterator>
#include <regex>


namespace day3{

bool isPartNumber(int row_pos, int col_pos, std::vector<std::string>& matrix) {
    const std::size_t row_start = std::max(row_pos - 1, 0);
    const std::size_t row_end = std::min(row_pos + 1, static_cast<int>(matrix.size() - 1));
    const std::size_t col_start = std::max(col_pos - 1, 0);
    const std::size_t col_end = std::min(col_pos + 1, static_cast<int>(matrix[0].length() - 1));
    for(std::size_t r = row_start; r <= row_end; ++r) {
        for(std::size_t c = col_start; c <= col_end; ++c) {
            if(const char letter = matrix[r][c]; !std::isdigit(letter) && letter != '.') {
                return true;
            }
        }
    }
    return false;
}

int solution1(const std::string& allInput){
    std::istringstream iss(allInput);
    std::string line;

    std::vector<std::string> matrix;
    while(std::getline(iss, line)){
        matrix.push_back(line);
    }
    int result = 0;
    for(std::size_t i = 0; i < matrix.size(); ++i){
        line = matrix[i];
        std::string acc = "";
        bool flag = false;
        for(std::size_t j = 0; j < line.length(); ++j){
            if(std::isdigit(line[j])) {
                acc += line[j];
                flag = flag || isPartNumber(i, j, matrix);
            }else {
                if(flag){ result += std::stoi(acc); }
                acc = "";
                flag = false;
            }
        }
        if(flag){result += std::stoi(acc);}
    }
    return result;
}

}