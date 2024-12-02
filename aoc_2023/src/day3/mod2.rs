use std::collections::HashMap;
use std::collections::HashSet;

use std::fs::read_to_string;
use std::cmp;

pub fn part1(){
    let mut part1 = 0;
    let mut part2 = 0;

    let path = "./src/day3/input_p1.txt";
    // let path = "./src/day3/example_p1.txt";
    let mut grid: Vec<Vec<char>> = vec![];
    for line in read_to_string( path ).unwrap().lines(){
        let line: Vec<char> = line.chars().collect();
        grid.push( line );
    }
    
    let xmax=grid.len()-1;
    let ymax=grid[0].len()-1;

    let mut size : usize=0;
    let mut all_gears: HashMap<(usize,usize), i32> = HashMap::new();

    for (x, line) in grid.iter().enumerate( ){
        for (y, c) in line.iter().enumerate( ){
            // println!("{x},{y} -> {c}");
            if c.is_numeric(){
                size += 1;
            }

            if ( ( ! c.is_numeric() ) || (y == ymax) ) && ( size > 0 ) {

                let mut is_part =false;
                let mut gears= HashSet::new();

                let imin= cmp::max( x as i32 -1, 0 ) as usize;
                let imax= cmp::min( x+1, xmax );
                let jmin= cmp::max( (y-size) as i32 -1, 0 ) as usize;
                let jmax= y;

                for i in imin..imax+1 {
                    for j in jmin..jmax+1 {
                        let c2=grid[i][j];
                        if ! c2.is_numeric() && c2 != '.' {
                            if c2 == '*'{
                                gears.insert((i,j));
                            }
                            is_part = true;
                        }
                    }
                }

                let mut number = 0;
                for c in line[(y-size)..y].iter(){
                    number = number * 10 + *c as i32 - '0' as i32;
                }

                println!("{number} {is_part}");

                if is_part {
                    part1+=number;
                }

                
                for g in gears.iter(){
                    if all_gears.contains_key(g){
                        part2 += number*all_gears[g];
                    } else {
                        all_gears.insert(*g, number );
                    }
                }
                size = 0;
            }
        }
    }
    println!("day3 part1: {part1}");
    println!("day3 part2: {part2}");
}


pub fn part2(){
}