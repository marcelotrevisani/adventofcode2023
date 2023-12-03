use std::collections::HashMap;

pub fn solution1(all_input: String) -> i32 {
    let mut result = 0;
    for line in all_input.lines() {
        result += get_first_and_last_numbers_from_string(line.to_string());
    }
    result
}

fn get_first_and_last_numbers_from_string(input: String) -> i32 {
    let first_number = input.chars().find(|&c| c.is_digit(10));
    let last_number = input.chars().rev().find(|&c| c.is_digit(10));
    let mut result = String::from(first_number.unwrap());
    result.push(last_number.unwrap());
    result.parse::<i32>().unwrap()
}

fn get_first_and_last_numbers_int_str_from_string(all_input: String) -> i32 {
    let map_str_int = HashMap::from([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);
    let mut min_pos = map_str_int.len() as i32;
    let mut max_pos = 0i32;
    let mut first_num = "";
    let mut last_num = "";
    for (word, value) in &map_str_int {
        let word_pos = all_input.find(word);
        let val_pos = all_input.find(value);

        if word_pos.is_some() {
            if min_pos > word_pos.unwrap() as i32 {
                min_pos = word_pos.unwrap() as i32;
                first_num = value;
            }
            if max_pos < word_pos.unwrap() as i32 {
                max_pos = word_pos.unwrap() as i32;
                last_num = value;
            }
        }
        if val_pos.is_some() {
            if min_pos > val_pos.unwrap() as i32 {
                min_pos = val_pos.unwrap() as i32;
                first_num = value;
            }
            if max_pos < val_pos.unwrap() as i32 {
                max_pos = val_pos.unwrap() as i32;
                last_num = value;
            }
        }
    }
    (first_num.to_string() + last_num).parse::<i32>().unwrap()
}
pub fn solution2(all_input: String) -> i32 {
    let mut result = 0;
    for line in all_input.lines() {
        result += get_first_and_last_numbers_int_str_from_string(line.to_string());
    }
    result
}
