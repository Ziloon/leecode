pub struct Solution;
impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut cnt = 0;
        let m = grid[0].len();
        let mut j= m;
        for row in &grid {
            while j > 0 && row[j-1] < 0 {
                j -= 1;
            }
            cnt += (m - j) as i32;
        }
        cnt
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_mixed() {
        // 示例 1: 标准混合矩阵
        let grid = vec![
            vec![4, 3, 2, -1],
            vec![3, 2, 1, -1],
            vec![1, 1, -1, -2],
            vec![-1, -1, -2, -3],
        ];
        assert_eq!(Solution::count_negatives(grid), 8);
    }

    #[test]
    fn test_case_all_positive() {
        // 示例 2: 全是正数
        let grid = vec![vec![3, 2], vec![1, 0]];
        assert_eq!(Solution::count_negatives(grid), 0);
    }

    #[test]
    fn test_case_all_negative() {
        // 额外情况: 全是负数
        let grid = vec![vec![-1, -1], vec![-2, -2]];
        assert_eq!(Solution::count_negatives(grid), 4);
    }

    #[test]
    fn test_case_single_element() {
        // 边界: 只有一个负数
        let grid = vec![vec![-1]];
        assert_eq!(Solution::count_negatives(grid), 1);
    }
}