#ifndef DAY3_H
#define DAY3_H

#include <string>

namespace day3{
    int solution1(const std::string& allInput);
    bool isPartNumber(int row_pos, int col_pos, std::vector<std::string>& matrix);
    int solution2(const std::string& allInput);
    int getGearRatio(size_t row_pos, size_t col_pos, std::vector<std::string>& matrix);
}

#endif
