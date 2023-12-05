#include "day3.h"
#include "utils.h"
#include <gtest/gtest.h>
#include <filesystem>

namespace day3 {
    TEST(Day3Solution1Test, Solution1_simples) {
        std::string all_input("467..114..\n\
...*......\n\
..35..633.\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598..");
        EXPECT_EQ(4361, solution1(all_input));
    }

    TEST(Day3Solution1Test, Solution1) {
        std::filesystem::path pathObj(__FILE__);
        pathObj.replace_filename("day3_input.txt");
        std::string allInput = utils::readFileContents(pathObj.string());

        EXPECT_EQ(538046, solution1(allInput));
    }

    TEST(Day3Solution2Test, Solution2_simples) {
        std::string all_input("467..114..\n\
...*......\n\
..35..633.\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598..");
        EXPECT_EQ(467835, solution2(all_input));
    }

    TEST(Day3Solution2Test, Solution2) {
        std::filesystem::path pathObj(__FILE__);
        pathObj.replace_filename("day3_input.txt");
        std::string allInput = utils::readFileContents(pathObj.string());

        EXPECT_EQ(81709807, solution2(allInput));
    }

}