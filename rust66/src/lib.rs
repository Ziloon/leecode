pub struct Solution;
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut digits = digits;
        for i in (0..digits.len()).rev() {
            if digits[i] < 9 {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        digits.insert(0, 1);
        let mut res = Vec::with_capacity(digits.len());
        res.push(1);
        res.extend(&digits);
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = Solution::plus_one(vec![1,2,3]);
        assert_eq!(vec![1,2,4], result);
    }

    #[test]
    fn check_various_length() {
        let result = Solution::plus_one(vec![4,3,2,1]);
        assert_eq!(vec![4,3,2,2], result);
    }

    #[test]
    fn check_carry_calculation() {
        let result = Solution::plus_one(vec![9]);
        assert_eq!(vec![1,0], result);
    }
}
