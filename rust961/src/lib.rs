use std::collections::HashSet;

pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
    let mut rec = HashSet::new();
    for num in nums {
        if !rec.insert(num) {
            return num;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = repeated_n_times(vec![1,2,3,3]);
        assert_eq!(3, result);
    }
}
