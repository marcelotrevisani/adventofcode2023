#include "day2.h"
#include "utils.h"
#include <gtest/gtest.h>
#include <fstream>
#include <sstream>
#include <string>
#include <filesystem>

namespace day2{

    TEST(Day2Solution1Test, Solution1_simples) {
        std::string all_input("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n\
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n\
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n\
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
        EXPECT_EQ(8, solution1(all_input));
    }

    TEST(Day2Solution2Test, Solution2_simples) {
        std::string all_input("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n\
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n\
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n\
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
        EXPECT_EQ(2286, solution2(all_input));
    }

    TEST(Day2Solution1Test, Solution1) {
        std::filesystem::path pathObj(__FILE__);
        pathObj.replace_filename("day2_input.txt");
        std::string allInput = utils::readFileContents(pathObj.string());

        EXPECT_EQ(2685, solution1(allInput));
    }

    TEST(Day2Solution2Test, Solution2) {
        std::filesystem::path pathObj(__FILE__);
        pathObj.replace_filename("day2_input.txt");
        std::string allInput = utils::readFileContents(pathObj.string());

        EXPECT_EQ(83707, solution2(allInput));
    }

}