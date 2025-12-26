struct Solution;
impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        // 1. Sort descending. sort_unstable is faster than sort.
        happiness.sort_unstable_by(|a, b| b.cmp(a));

        let k = k as usize;

        // 2. Use a functional approach for speed and clarity
        happiness
            .into_iter()
            .enumerate()
            .take(k) // Only consider the first k elements
            .map(|(i, val)| (val - i as i32) as i64) // Calculate current happiness
            .take_while(|&current| current > 0) // Early exit: stop if happiness is 0 or less
            .sum() // Add them up
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        // happiness = [1,2,3], k = 2 -> output: 4
        let happiness = vec![1, 2, 3];
        assert_eq!(Solution::maximum_happiness_sum(happiness, 2), 4);
    }

    #[test]
    fn test_example_2() {
        // happiness = [1,1,1,1], k = 2 -> output: 1
        let happiness = vec![1, 1, 1, 1];
        assert_eq!(Solution::maximum_happiness_sum(happiness, 2), 1);
    }

    #[test]
    fn test_example_3() {
        // happiness = [2,3,4,5], k = 1 -> output: 5
        let happiness = vec![2, 3, 4, 5];
        assert_eq!(Solution::maximum_happiness_sum(happiness, 1), 5);
    }

    #[test]
    fn test_all_zeros() {
        // Test when values become zero quickly
        let happiness = vec![1, 1];
        assert_eq!(Solution::maximum_happiness_sum(happiness, 2), 1);
    }

    #[test]
    fn test_large_values() {
        // Test large integers to ensure i64 prevents overflow
        let happiness = vec![100000000, 100000000];
        assert_eq!(Solution::maximum_happiness_sum(happiness, 2), 199999999);
    }
}
