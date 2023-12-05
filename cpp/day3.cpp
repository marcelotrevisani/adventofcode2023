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
    unsigned long result = 0;
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

int solution2(const std::string& allInput) {
    std::istringstream iss(allInput);
    std::string line;

    std::vector<std::string> matrix;
    while(std::getline(iss, line)){
        matrix.push_back(line);
    }
    int result = 0;
    for(std::size_t i = 0; i < matrix.size(); ++i) {
        line = matrix[i];
        for(std::size_t j = 0; j < line.length(); ++j) {
            if(line[j] == '*') {
                result += getGearRatio(i, j, matrix);
            }
        }
    }
    return result;
}

int getGearRatio(size_t row_pos, size_t col_pos, std::vector<std::string>& matrix) {
    std::regex re_num("(\\d+)");
    std::vector<int> result;
    for(size_t i = row_pos - 1; i <= row_pos + 1; ++i) {
        const std::string line = matrix[i];
        for(std::sregex_iterator it = std::sregex_iterator(line.begin(), line.end(), re_num);
     it != std::sregex_iterator(); ++it) {
            std::smatch match = *it;
            size_t start_pos = match.position();
            size_t end_pos = start_pos + match.str().length() - 1;
            if((start_pos >= col_pos - 1 && start_pos <= col_pos + 1) || (end_pos >= col_pos - 1 && end_pos <= col_pos + 1)) {
                result.push_back(std::stoi(match.str()));
            }
        }
    }
    if(result.size() != 2) {
        return 0;
    }
    return result[0] * result[1];
}

}