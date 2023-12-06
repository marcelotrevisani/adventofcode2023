#include "day4.h"
#include <string>
#include <sstream>
#include <iterator>
#include <regex>
#include <set>
#include <algorithm>
#include <numeric>


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

    int solution2(const std::string& all_input) {
        std::istringstream iss(all_input);
        std::string line;
        int num_lines = std::count(all_input.begin(), all_input.end(), '\n') + 1;
        unsigned int result[num_lines];
        std::fill_n(result, num_lines, 1);

        for(size_t pos=0; std::getline(iss, line); ++pos){
            unsigned int num_winners = countWinningNumbers(line);
            if(num_winners == 0) {
                continue;
            }
            for(size_t start=pos + 1; start < num_lines && num_winners > 0; --num_winners, ++start) {
                result[start] += result[pos];
            }
            if(num_winners  > 0) {
                result[num_lines - 1] += num_winners;
            }
        }
        return std::accumulate(result, result + num_lines, 0);
    }


    int countWinningNumbers(const std::string& line) {
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
        return num_win_numbers;
    }

    int getPointsByCard(const std::string& line) {
        int num_win_numbers = countWinningNumbers(line);
        return static_cast<int>(std::pow(2, num_win_numbers - 1));
    }


}
