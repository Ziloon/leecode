use std::collections::HashSet;

pub struct Solution;

impl Solution {
    fn dfs(i:usize, cur_col:&str, next_col:&mut String, allowed_map:&[[u8;6];6], invalid_rec:&mut HashSet<String>) -> bool {
        if cur_col.len() == 1 {
            return true;
        }
        if i == 0 && invalid_rec.contains(cur_col) {
            return false;
        }
        if i == cur_col.len()-1 {
            let mut new_next_col = String::new();
            return Self::dfs(0, next_col, &mut new_next_col, allowed_map, invalid_rec);
        }
        let left = (cur_col.as_bytes()[i] - b'A') as usize;
        let right = (cur_col.as_bytes()[i+1] - b'A') as usize;
        if left >= 6 || right >= 6 { return false; }
        for top in 0..6 {
            if (allowed_map[left][right] & 1u8 << (top as usize)) != 0u8 {
                next_col.push((top+'A' as u8) as char);
                if Self::dfs(i+1, cur_col, next_col, allowed_map, invalid_rec) {
                    return true;
                }

                next_col.pop();
            }
        }
        if i == 0 {
            invalid_rec.insert(cur_col.to_string());
        }
        false
    }

    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        let mut allowed_map = [[0u8;6];6];
        for s in allowed {
            let bytes = s.as_bytes();
            let left = (bytes[0] - b'A') as usize;
            let right = (bytes[1] - b'A') as usize;
            let top = (bytes[2] - b'A') as usize;
            if top >= 6 {
                continue;
            }
            allowed_map[left][right] |= 1u8 << top;
        }
        let mut invalid_rec:HashSet<String> = HashSet::new();
        let mut next_col: String = String::new();
        Self::dfs(0, &bottom, &mut next_col, &allowed_map, &mut invalid_rec)
    }
}

#[cfg(test)]
mod tests {
    use super::*; // 导入外部定义的 Solution 结构

    #[test]
    fn test_pyramid_success() {
        let bottom = "BCD".to_string();
        let allowed = vec!["BCC".to_string(), "CDE".to_string(), "CEA".to_string(), "FFF".to_string()];
        // 逻辑：BC->C, CD->E => 上层是 CE; CE->A => 塔尖是 A
        assert_eq!(Solution::pyramid_transition(bottom, allowed), true);
    }

    #[test]
    fn test_pyramid_failure() {
        let bottom = "AAAA".to_string();
        let allowed = vec!["AAB".to_string(), "AAC".to_string(), "BCD".to_string(), "BBE".to_string()];
        // 逻辑：虽然底层有很多 A，但可能无法凑齐覆盖所有相邻对的规则
        assert_eq!(Solution::pyramid_transition(bottom, allowed), false);
    }

    #[test]
    fn test_multiple_options() {
        // 测试存在多种选择时，是否能通过回溯找到正确的那条路
        let bottom = "AAB".to_string();
        let allowed = vec![
            "AAA".to_string(), "AAB".to_string(), // AA 可以变 A 或 B
            "ABA".to_string(), "ABB".to_string(), // AB 可以变 A 或 B
            "ABZ".to_string()                     // 假设塔尖需要 Z
        ];
        // 即使有干扰项，只要有一条路通向塔尖，就应返回 true
        assert_eq!(Solution::pyramid_transition(bottom, allowed), true);
    }
}