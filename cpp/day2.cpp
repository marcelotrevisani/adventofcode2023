#include "day2.h"
#include <string>
#include <sstream>
#include <iterator>
#include <regex>
#include <unordered_map>

namespace day2{
int solution1(const std::string& allInput){
    std::istringstream iss(allInput);
    std::string line;
    int result = 0;
    while(std::getline(iss, line)){
        result += getValidGame(line);
    }
    return result;
}

int getValidGame(const std::string& line) {
    std::regex re_game("Game\\s+(\\d+)");
    std::smatch matchGame;
    std::regex_search(line, matchGame, re_game);
    int gameId = std::stoi(matchGame.str(1));

    std::regex re_blocks("(\\d+)\\s+(red|green|blue)");
    std::stringstream lineStrem(line);
    std::string block;
    std::vector<std::string> listBlocks;

    std::pmr::unordered_map<std::string, int> colorBlocks = {
        {"red", 12},
        {"green", 13},
        {"blue", 14},
    };

    while(std::getline(lineStrem, block, ';')){
        std::smatch matchBlock;
        for (std::sregex_iterator it = std::sregex_iterator(block.begin(), block.end(), re_blocks);
     it != std::sregex_iterator(); ++it){
            std::smatch colVal = *it;
            int colorValue = std::stoi(colVal.str(1));
            if(colorValue > colorBlocks[colVal.str(2)]){
                return 0;
            }
        }
    }
    return gameId;
}

int solution2(const std::string& allInput) {
    std::istringstream iss(allInput);
    std::string line;
    int result = 0;
    while(std::getline(iss, line)){
        result += getPowerBlocks(line);
    }
    return result;
}

int getPowerBlocks(const std::string& line) {
    std::pmr::unordered_map<std::string, int> colorBlocks = {
        {"red", 0},
        {"green", 0},
        {"blue", 0},
    };
    std::regex re_blocks("(\\d+)\\s+(red|green|blue)");
    std::stringstream lineStream(line);
    std::string block;
    std::vector<std::string> listBlocks;
    while(std::getline(lineStream, block, ';')){
        std::smatch matchBlock;
        for (std::sregex_iterator it = std::sregex_iterator(block.begin(), block.end(), re_blocks);
     it != std::sregex_iterator(); ++it){
            std::smatch colVal = *it;
            colorBlocks[colVal.str(2)] = std::max(std::stoi(colVal.str(1)), colorBlocks[colVal.str(2)]);
        }
    }
    return colorBlocks["red"] * colorBlocks["green"] * colorBlocks["blue"];
}

}
