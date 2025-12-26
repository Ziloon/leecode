pub struct Solution;
impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let bytes = customers.as_bytes();

        // 1. 初始代价：假设第 0 小时关门
        // 此时代价 = 所有的 'Y'（因为所有客人都被错过了）
        let mut current_penalty: i32 = bytes.iter().filter(|&&b| b == b'Y').count() as i32;

        let mut min_penalty = current_penalty;
        let mut best_hour = 0;

        // 2. 逐小时向后移动关门时间
        for (i, &customer) in bytes.iter().enumerate() {
            if customer == b'Y' {
                // 如果当前是 'Y'，我们晚一小时关门，就接到了这个客人
                // 代价减少 1
                current_penalty -= 1;
            } else {
                // 如果当前是 'N'，我们晚一小时关门，就多了一小时空等
                // 代价增加 1
                current_penalty += 1;
            }

            // 3. 比较并记录。注意：这里用 < 而不是 <=，保证相同代价取最早的时间
            if current_penalty < min_penalty {
                min_penalty = current_penalty;
                best_hour = (i + 1) as i32;
            }
        }

        best_hour
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        // 示例 1: "YYNY" -> 第 2 小时关门代价为 1（最小）
        assert_eq!(Solution::best_closing_time("YYNY".to_string()), 2);
    }

    #[test]
    fn test_case_2() {
        // 示例 2: "NNNN" -> 第 0 小时关门代价为 0
        assert_eq!(Solution::best_closing_time("NNNN".to_string()), 0);
    }

    #[test]
    fn test_case_3() {
        // 示例 3: "YYYY" -> 第 4 小时关门代价为 0
        assert_eq!(Solution::best_closing_time("YYYY".to_string()), 4);
    }
}