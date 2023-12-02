#include "day1.h"
#include <regex>
#include <sstream>
#include <string>
#include <iterator>

namespace day1{

int solution1(const std::string& allInput){
    std::istringstream iss(allInput);
    std::string line;
    int result = 0;
    while(std::getline(iss, line)){
        result += day1::getNumberFromLine(line);
    }
    return result;
}

int getNumberFromLine(const std::string& line){
    std::regex re_numbers("(\\d)");
    auto begin = std::sregex_iterator(line.begin(), line.end(), re_numbers);
    auto num_matches = std::distance(begin, std::sregex_iterator());
    std::smatch firstMatch = *begin;
    std::advance(begin, num_matches - 1);
    std::smatch lastMatch = *begin;
    std::string numberStr = firstMatch.str() + lastMatch.str();
    return std::stoi(numberStr);
}
}