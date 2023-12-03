extern crate adoc2023;
use adoc2023::day1::{solution1, solution2};
use std::fs;
use std::path::PathBuf;

#[test]
fn test_solution1_simple() {
    let all_input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet";
    assert_eq!(solution1(all_input.to_string()), 142);
}

#[test]
fn test_solution1() {
    let file_path = PathBuf::from("tests/data/day1.txt");
    let all_input = fs::read_to_string(file_path).expect("Failed to read file");
    assert_eq!(solution1(all_input.to_string()), 54927);
}

#[test]
fn test_solution2_simple() {
    let all_input = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen";
    assert_eq!(solution2(all_input.to_string()), 281);
}
