use regex::Regex;
use std::cmp;
use std::collections::HashMap;

pub fn solution1(all_input: String) -> i32 {
    let mut result = 0;
    for line in all_input.lines() {
        result += get_valid_game_id(line.to_string());
    }
    result
}

fn get_valid_game_id(line: String) -> i32 {
    let limit_blocks = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let re_game = Regex::new(r"Game\s+(\d+)").unwrap();
    let re_blocks = Regex::new(r"(\d+)\s+(red|green|blue)").unwrap();
    let game_id = re_game
        .captures(&line)
        .unwrap()
        .get(1)
        .unwrap()
        .as_str()
        .parse::<i32>()
        .unwrap();
    for blocks in line.split(";") {
        for color_block in re_blocks.captures_iter(&blocks) {
            let val_color = color_block.get(1).unwrap().as_str().parse::<i32>().unwrap();
            let name_color = color_block.get(2).unwrap().as_str();
            if val_color > limit_blocks[name_color] {
                return 0;
            }
        }
    }
    game_id
}

fn get_valid_game_id_with_min_blocks(line: String) -> i32 {
    let re_blocks = Regex::new(r"(\d+)\s+(red|green|blue)").unwrap();
    let mut min_blocks = HashMap::new();
    for blocks in line.split(";") {
        for color_block in re_blocks.captures_iter(&blocks) {
            let val_color = color_block.get(1).unwrap().as_str().parse::<i32>().unwrap();
            let name_color = color_block.get(2).unwrap().as_str();
            if let Some(value) = min_blocks.get_mut(name_color) {
                *value = cmp::max(*value, val_color);
            } else {
                min_blocks.insert(name_color, val_color);
            }
        }
    }
    min_blocks.values().product()
}

pub fn solution2(all_input: String) -> i32 {
    let mut result = 0;
    for line in all_input.lines() {
        result += get_valid_game_id_with_min_blocks(line.to_string());
    }
    result
}
