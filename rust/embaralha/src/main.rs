use json;
use std::{collections::VecDeque, env};

fn main() {
    let args: Vec<_> = env::args().collect();
    let n = args[1].parse::<i32>().unwrap();
    let (deck, card) = embaralha(n);
    print_result(deck, card);
}

fn print_result(a: Vec<i32>, b: i32) {
    // print!("[");
    // // for i in a {
    // //     print!("{} ", i);
    // // }
    // // println!("\u{8}] {}", b);
    // let last_index = a.len() - 1;
    // for i in 0..last_index {
    //     print!("{} ", a[i]);
    // }
    // println!("{}] {}", a[last_index], b);

    // print!("[");
    // print!("{:?}", a);
    // print!(", ");
    // print!("{:?}", b);
    // println!("]");

    // println!("{:#?}", (a, b));

    let mut data = json::JsonValue::new_array();
    _ = data.push(a);
    _ = data.push(b);
    println!("{}", data.dump());
    
    //print!("[[");
    //let last_index = a.len() - 1;
    //for i in 0..last_index {
    //    print!("{},", a[i]);
    //}
    //println!("{}],{}]", a[last_index], b);
}

fn embaralha(n: i32) -> (Vec<i32>, i32) {
    let mut initial_deck = VecDeque::with_capacity(n as usize);
    for i in 0..n {
        initial_deck.push_back(i + 1)
    }
    let mut remaning_cards = vec![];
    while initial_deck.len() > 1 {
        remaning_cards.push(initial_deck.pop_front().unwrap());
        let front_card = initial_deck.pop_front().unwrap();
        initial_deck.push_back(front_card);
    }
    let last_card = initial_deck[0];
    (remaning_cards, last_card)
}

// Essa ideia de loop falhou, não pela programação, mas pela ideia mesmo.
// fn embaralha2(n: i32) -> (Vec<i32>, i32) {
//     let mut initial_deck: VecDeque<i32> = VecDeque::with_capacity(n as usize);
//     for i in 0..n {
//         initial_deck.push_back(i + 1)
//     }
//     let mut remaning_cards = vec![];
//     let mut len_initial_deck = b1.len();
//     while len_initial_deck > 1 {
//         let n2 = match len_initial_deck % 2 == 0 {
//             true => len_initial_deck / 2,
//             false => len_initial_deck / 2 + 1,
//         };
//         // let n2 = len_initial_deck / 2;
//         for i in 0..n2 {
//             // remaning_cards.push(initial_deck[i]);
//             remaning_cards.push(initial_deck.remove(i).unwrap());
//         }
//         len_initial_deck = b1.len();
//     }
//     let last_card = initial_deck[0];
//     (remaning_cards, last_card)
// }
