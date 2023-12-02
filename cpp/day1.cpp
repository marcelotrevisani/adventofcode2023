#include "day1.h"
#include <regex>
#include <sstream>
#include <string>
#include <iterator>
#include <unordered_map>

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

int solution2(const std::string& allInput) {
    std::istringstream iss(allInput);
    std::string line;
    int result = 0;
    while(std::getline(iss, line)){
        result += getNumberOrNameFromLine(line);
    }
    return result;
}

int getNumberOrNameFromLine(const std::string& line) {
    std::unordered_map<std::string, std::string> mapInts = {
        {"one", "1"},
        {"two", "2"},
        {"three", "3"},
        {"four", "4"},
        {"five", "5"},
        {"six", "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine", "9"}
    };
    std::regex re_numbers("(?=(\\d|one|two|three|four|five|six|seven|eight|nine))");
    auto begin = std::sregex_iterator(line.begin(), line.end(), re_numbers);
    auto num_matches = std::distance(begin, std::sregex_iterator());

    std::smatch firstMatch = *begin;
    std::string firstMatchStr = firstMatch.str(1);
    std::advance(begin, num_matches - 1);
    std::smatch lastMatch = *begin;
    std::string lastMatchStr = lastMatch.str(1);
    if(firstMatchStr.size() > 1) {
        firstMatchStr = mapInts[firstMatchStr];
    }
    if(lastMatchStr.size() > 1) {
        lastMatchStr = mapInts[lastMatchStr];
    }
    return std::stoi(firstMatchStr + lastMatchStr);
}

}