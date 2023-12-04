extern crate adoc2023;

use adoc2023::day2::{solution1, solution2};
use std::fs;
use std::path::PathBuf;

#[test]
fn test_solution1_simple() {
    let all_input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
    assert_eq!(solution1(all_input.to_string()), 8);
}

#[test]
fn test_solution1() {
    let file_path = PathBuf::from("tests/data/day2.txt");
    let all_input = fs::read_to_string(file_path).expect("Failed to read file");
    assert_eq!(solution1(all_input.to_string()), 2685);
}

#[test]
fn test_solution2_simple() {
    let all_input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
    assert_eq!(solution2(all_input.to_string()), 2286);
}

#[test]
fn test_solution2() {
    let file_path = PathBuf::from("tests/data/day2.txt");
    let all_input = fs::read_to_string(file_path).expect("Failed to read file");
    assert_eq!(solution2(all_input.to_string()), 83707);
}
