class Solution {
public:
    bool isPalindrome(int x) {
        string num = to_string(x);
        for (int i = 0; i < num.length(); ++i) {
            if (num[i] != num[num.length()-i-1]) {
                return false;
            }
        }
        return true;
    }
};