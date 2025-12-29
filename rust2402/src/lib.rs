use std::cmp::Reverse;
use std::collections::BinaryHeap;
pub struct Solution;
impl Solution {

    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let mut idx: Vec<usize> = (0..meetings.len()).collect();
        idx.sort_unstable_by_key(|&i| meetings[i][0]);

        let mut unused: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        for i in 0..n {
            unused.push(Reverse(i));
        }

        let mut engaged: BinaryHeap<Reverse<(i64, i32)>> = BinaryHeap::new();
        let mut room_cnt: Vec<i32> = vec![0; n as usize];
        for i in idx {
            let start = meetings[i][0] as i64;
            let end = meetings[i][1] as i64;
            let duration = end - start;

            while let Some(Reverse((end_time, _))) = engaged.peek() {
                if *end_time <= start {
                    let Reverse((_, id)) = engaged.pop().unwrap();
                    unused.push(Reverse(id));
                } else {
                    break;
                }
            }

            if let Some(Reverse(room_id)) = unused.pop() {
                room_cnt[room_id as usize] += 1;
                engaged.push(Reverse((end, room_id)));
            } else if let Some(Reverse((ealist_end, room_id))) = engaged.pop() {
                room_cnt[room_id as usize] += 1;
                engaged.push(Reverse((ealist_end + duration, room_id)));
            }
        }
        let mut room_max = -1;
        let mut res:i32 = 0;
        for (i, &c) in room_cnt.iter().enumerate() {
            if c > room_max {
                room_max = c;
                res = i as i32;
            }
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

}
