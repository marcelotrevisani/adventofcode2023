#include "day4.h"
#include <string>
#include <sstream>
#include <iterator>
#include <regex>
#include <set>


namespace day4 {
    int solution1(const std::string& all_input) {
        std::istringstream iss(all_input);
        std::string line;
        int result = 0;
        while(std::getline(iss, line)){
            result += getPointsByCard(line);
        }
        return result;
    }

    int getPointsByCard(const std::string& line) {
        auto pos_colon = line.find_first_of(":");
        auto pos_pipe = line.find_first_of("|");
        std::regex re_num("(\\d+)");
        std::set<int> all_winning_numbers;

        for(
            std::sregex_iterator it = std::sregex_iterator(line.begin() + pos_colon + 1, line.begin() + pos_pipe - 1, re_num);
            it != std::sregex_iterator();
            ++it
        ) {
            std::smatch match = *it;
            all_winning_numbers.insert(std::stoi(match.str()));
        }
        int num_win_numbers = 0;
        for(
            std::sregex_iterator it = std::sregex_iterator(line.begin() + pos_pipe + 1, line.end(), re_num);
            it != std::sregex_iterator();
            ++it
        ) {
            std::smatch match = *it;
            int num = std::stoi(match.str());
            if(all_winning_numbers.count(num)) {
                num_win_numbers++;
            }
        }
        if(num_win_numbers == 0) {
            return 0;
        }
        return static_cast<int>(std::pow(2, num_win_numbers - 1));
    }


}