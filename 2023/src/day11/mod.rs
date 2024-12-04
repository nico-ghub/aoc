use std::{fs::read_to_string, collections::HashSet};

pub fn part1(){
    let mut result = 0;
    let path = "./src/day11/input_p1.txt";
    let path = "./src/day11/example_p1.txt";
    let mut g :  Vec<(usize,usize)> = vec![];
    let mut dx: HashSet<usize> = HashSet::new();
    let mut dy = 0;

    for (y, line) in read_to_string( path ).unwrap().lines().enumerate(){
        if line.contains('#'){
            for (x, c) in line.chars().enumerate(){
                if c == '#' {
                    g.push( (x,y+dy));
                    dx.insert(x);
                }
            }
        } else {
            dy+=1;
        }
    }
    let dx = (0..*g.iter().map(|(x,y)|x).max().unwrap()+1 ).into_iter().map( |i| i - dx.iter().filter(|j| **j < i ).count() ).collect::<Vec<_>>();
    // for ( x,y ) in & mut g {
    //     *x+=dx[*x];
    //     println!("{x} {y}");
    // }
    for (i, ( x,y ) ) in g.iter().enumerate() {
        
    }
}

pub fn part2(){
    let mut result = 0;
    let path = "./src/day11/input_p1.txt";
    let path = "./src/day11/example_p2.txt";
    for line in read_to_string( path ).unwrap().lines(){
    
    }
    println!("day11 part2: {result}");
}