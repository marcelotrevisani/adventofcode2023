#include "day1.h"
#include <gtest/gtest.h>
#include <fstream>
#include <sstream>
#include <string>
#include <filesystem>

namespace day1 {

    TEST(Day1Test, GetNumberFromLine) {
        EXPECT_EQ(13, getNumberFromLine("abc1def2ghi3"));
        EXPECT_EQ(14, getNumberFromLine("1234"));
    }

    TEST(Day1Test, Solution1_simples) {
        std::string input1 = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet";
        EXPECT_EQ(142, solution1(input1));
    }

    std::string readFileContents(const std::string& filePath) {
        std::ifstream fileStream(filePath);
        if (!fileStream) {
            std::cerr << "Failed to open file: " << filePath << std::endl;
            return "";
        }
        std::stringstream buffer;
        buffer << fileStream.rdbuf();
        return buffer.str();
    }

    TEST(Day1Test, Solution1) {
        std::filesystem::path pathObj(__FILE__);
        pathObj.replace_filename("day1_input.txt");
        std::string allInput = readFileContents(pathObj.string());

        EXPECT_EQ(54927, solution1(allInput));
    }
}
