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
